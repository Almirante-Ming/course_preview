from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from datetime import datetime, timedelta, UTC
from typing import Optional, Dict
from pydantic import BaseModel
import bcrypt
import secrets
import hashlib
import base64

app = FastAPI()


SECRET_KEY = "im_be_back"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7

CLIENT_ID = "t1000"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/oauth/token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: Optional[str] = None
    full_name: Optional[str] = None


def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

fake_users_db: Dict[str, UserInDB] = {
    "mobile_user": UserInDB(
        username="mobile_user",
        hashed_password="$2b$12$zEmkpl0gye2uTvRQlvtdeO73Ebbl1CwB4a3tLhJq2kd9cB13Rulx2", # Senha: password123
        email="mobile@example.com",
        full_name="Usuário Mobile Teste"
    ),
    "test_user": UserInDB(
        username="test_user",
        hashed_password="$2b$12$s9mK5s7E2A1yexG2DX56QOHc/uBY5rbH.VEN2S6kFOlX7qeqvM82O", # Senha: secure_pass
        email="test@example.com",
        full_name="Usuário de Teste"
    )
}

in_memory_tokens: Dict[str, Dict[str, str | datetime]] = {}

pkce_code_verifiers: Dict[str, str] = {}

def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None, token_type: str = "access"):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        if token_type == "access":
            expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        else:
            expire = datetime.now(UTC) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    to_encode.update({"exp": expire, "type": token_type})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt, expire

def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def get_user(username: str):
    return fake_users_db.get(username)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_jwt_token(token)
    if payload is None or payload.get("type") != "access":
        raise credentials_exception
    
    username: str = payload.get("sub") 
    if username is None:
        raise credentials_exception
    
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user

def generate_random_string(length: int):
    return secrets.token_urlsafe(length)

def sha256_hash(input_string: str):
    return hashlib.sha256(input_string.encode('utf-8')).digest()

def base64url_encode(data: bytes):
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('ascii')

@app.get("/")
async def read_root():
    return {"message": "API de Teste de Login - Status: OK"}

@app.get("/oauth/authorize")
async def authorize_user(
    client_id: str,
    redirect_uri: str,
    response_type: str = "code",
    scope: str = "",
    state: Optional[str] = None,
    code_challenge: Optional[str] = None,
    code_challenge_method: Optional[str] = None
):
    if client_id != CLIENT_ID:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client ID inválido"
        )
    if response_type != "code":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="response_type deve ser 'code'"
        )
    if code_challenge and code_challenge_method != "S256":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="code_challenge_method deve ser 'S256' se code_challenge for fornecido"
        )
    
    # Gerar um código de autorização temporário
    authorization_code = secrets.token_urlsafe(32)
    
    # Armazenar o code_challenge (se PKCE for usado) associado ao código de autorização
    if code_challenge:
        pkce_code_verifiers[authorization_code] = code_challenge
        print(f"PKCE: code_challenge '{code_challenge}' armazenado para code '{authorization_code}'")

    # Construir o URI de redirecionamento com o código de autorização e o estado
    redirect_url = f"{redirect_uri}?code={authorization_code}"
    if state:
        redirect_url += f"&state={state}"
    
    print(f"Redirecionando para: {redirect_url}")
    return RedirectResponse(url=redirect_url, status_code=status.HTTP_302_FOUND)

@app.post("/oauth/token", response_model=dict)
async def get_oauth_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.grant_type == "password":
        user = get_user(form_data.username)
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Nome de usuário ou senha incorretos",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token, access_expires_at = create_jwt_token(data={"sub": user.username}, token_type="access")
        refresh_token, refresh_expires_at = create_jwt_token(data={"sub": user.username}, token_type="refresh", expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
        
        in_memory_tokens[user.username] = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "access_token_expires_at": access_expires_at,
            "refresh_token_expires_at": refresh_expires_at
        }
        print(f"Tokens para '{user.username}' gerados e armazenados (password grant).")

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            "refresh_token": refresh_token
        }


    elif form_data.grant_type == "authorization_code":
        code = form_data.code
        code_verifier = form_data.code_verifier
        
        if not code or not code_verifier:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Código de autorização ou code_verifier ausente."
            )
        
        # Verificar o code_verifier contra o code_challenge armazenado
        stored_code_challenge = pkce_code_verifiers.pop(code, None)
        if not stored_code_challenge:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Código de autorização inválido ou já usado."
            )
        
        # Recalcular o code_challenge do verifier recebido e comparar
        calculated_code_challenge = base64url_encode(sha256_hash(code_verifier))
        
        if calculated_code_challenge != stored_code_challenge:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="code_verifier inválido."
            )
        
        user = fake_users_db["mobile_user"]
        
        access_token, access_expires_at = create_jwt_token(data={"sub": user.username}, token_type="access")
        refresh_token, refresh_expires_at = create_jwt_token(data={"sub": user.username}, token_type="refresh", expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
        
        in_memory_tokens[user.username] = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "access_token_expires_at": access_expires_at,
            "refresh_token_expires_at": refresh_expires_at
        }
        print(f"Tokens para '{user.username}' gerados e armazenados (authorization code grant).")

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            "refresh_token": refresh_token
        }
    
    elif form_data.grant_type == "refresh_token":
        refresh_token = form_data.refresh_token
        if not refresh_token:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Refresh token ausente."
            )
        
        payload = decode_jwt_token(refresh_token)
        if payload is None or payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token inválido ou expirado."
            )
        
        username = payload.get("sub")
        if not username or username not in in_memory_tokens or in_memory_tokens[username].get("refresh_token") != refresh_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token não corresponde ou não encontrado."
            )
        
 
        user = get_user(username)
        access_token, access_expires_at = create_jwt_token(data={"sub": user.username}, token_type="access")
        
        in_memory_tokens[username]["access_token"] = access_token
        in_memory_tokens[username]["access_token_expires_at"] = access_expires_at
        print(f"Access token para '{username}' renovado.")

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
        }

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tipo de concessão (grant_type) não suportado."
        )

@app.get("/oauth/userinfo", response_model=dict)
async def get_user_info(current_user: UserInDB = Depends(get_current_user)):
    return {
        "sub": current_user.username,
        "name": current_user.full_name,
        "email": current_user.email,
        "preferred_username": current_user.username,
    }

@app.post("/oauth/revoke")
async def revoke_token(token: str = Depends(oauth2_scheme)):
    payload = decode_jwt_token(token)
    if payload and payload.get("sub"):
        username = payload["sub"]
        if username in in_memory_tokens:
            del in_memory_tokens[username]
            print(f"Tokens para '{username}' revogados com sucesso (simulado).")
            return {"message": "Token revogado com sucesso."}
    
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Token inválido ou não encontrado para revogação."
    )

@app.get("/api/protected-data")
async def get_protected_data(current_user: UserInDB = Depends(get_current_user)):
    return {
        "message": f"Olá, {current_user.username}.",
        "data": {
            "item1": "esta informacao esta segura",
            "item2": "aqui se encontra as coordedadas da skynet",
            "timestamp": datetime.now(UTC).isoformat()
        }
    }
