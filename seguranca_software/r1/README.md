# FastAPI OAuth2 Authentication Test Server

This is a comprehensive FastAPI application implementing OAuth2 authentication with multiple grant types for testing login endpoints.

## Features

- **OAuth2 Authorization Code Flow with PKCE** (recommended for mobile apps)
- **Resource Owner Password Credentials Grant** (traditional username/password login)
- **Refresh Token Grant** (for token renewal)
- **JWT-based authentication** with access and refresh tokens
- **Protected API endpoints** requiring authentication
- **In-memory user storage** with bcrypt password hashing
- **CORS support** for frontend integration

## Quick Start

### 1. Start the Server

```bash
# Using the startup script
./start_server.sh

# Or manually
.venv/bin/python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The server will be available at:
- **API Base URL**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc

### 2. Test the Authentication

Run the test script to verify all OAuth2 flows:

```bash
.venv/bin/python test_oauth.py
```

## Available Endpoints

### Authentication Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/oauth/authorize` | GET | Authorization endpoint for OAuth2 code flow |
| `/oauth/token` | POST | Token endpoint (supports multiple grant types) |
| `/oauth/userinfo` | GET | Get authenticated user information |
| `/oauth/revoke` | POST | Revoke access tokens |

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Health check |
| `/api/protected-data` | GET | Protected endpoint requiring authentication |

## Test Users

The application comes with pre-configured test users:

| Username | Password | Email | Full Name |
|----------|----------|-------|-----------|
| `mobile_user` | `password123` | mobile@example.com | Usuário Mobile Teste |
| `test_user` | `secure_pass` | test@example.com | Usuário de Teste |

## OAuth2 Grant Types

### 1. Password Grant (Traditional Login)

```bash
curl -X POST "http://localhost:8000/oauth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=password&username=mobile_user&password=password123"
```

### 2. Authorization Code Grant with PKCE

**Step 1**: Generate PKCE parameters
```python
import secrets, hashlib, base64

code_verifier = secrets.token_urlsafe(32)
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
).rstrip(b'=').decode('ascii')
```

**Step 2**: Authorization request
```
GET /oauth/authorize?client_id=your-actual-oauth2-client-id&redirect_uri=myapp://callback&response_type=code&scope=read write&state=random_state&code_challenge=CODE_CHALLENGE&code_challenge_method=S256
```

**Step 3**: Exchange code for tokens
```bash
curl -X POST "http://localhost:8000/oauth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code&code=AUTHORIZATION_CODE&code_verifier=CODE_VERIFIER&client_id=your-actual-oauth2-client-id"
```

### 3. Refresh Token Grant

```bash
curl -X POST "http://localhost:8000/oauth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token&refresh_token=REFRESH_TOKEN"
```

## Using Access Tokens

Include the access token in the Authorization header for protected endpoints:

```bash
curl -X GET "http://localhost:8000/api/protected-data" \
  -H "Authorization: Bearer ACCESS_TOKEN"
```

## Configuration

### Environment Variables (Recommended for Production)

```bash
export SECRET_KEY="your-super-secret-jwt-key"
export CLIENT_ID="your-oauth2-client-id"
export ACCESS_TOKEN_EXPIRE_MINUTES=60
export REFRESH_TOKEN_EXPIRE_DAYS=7
```

### Security Notes

⚠️ **Important for Production**:

1. **Change the SECRET_KEY**: Use a strong, random secret key
2. **Configure CORS properly**: Don't use `allow_origins=["*"]` in production
3. **Use HTTPS**: Always use HTTPS in production
4. **Use a real database**: Replace in-memory storage with a proper database
5. **Implement proper user management**: Add user registration, password reset, etc.
6. **Add rate limiting**: Implement rate limiting for authentication endpoints
7. **Log security events**: Add proper logging for authentication attempts

## Dependencies

- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `python-jose[cryptography]`: JWT handling
- `passlib[bcrypt]`: Password hashing
- `python-multipart`: Form data parsing
- `requests`: HTTP client for testing

## Development

### Adding New Users

Edit the `fake_users_db` dictionary in `main.py`:

```python
fake_users_db["new_user"] = UserInDB(
    username="new_user",
    hashed_password=get_password_hash("new_password"),
    email="new@example.com",
    full_name="New User"
)
```

### Adding New Protected Endpoints

```python
@app.get("/api/new-endpoint")
async def new_endpoint(current_user: UserInDB = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}!", "data": "..."}
```

## Testing with Mobile Apps

For mobile app integration:

1. Use the **Authorization Code flow with PKCE** for security
2. Configure your app to handle the redirect URI: `myapp://callback`
3. Store tokens securely in the mobile app
4. Implement token refresh before expiration
5. Handle authentication errors gracefully

## Troubleshooting

### Common Issues

1. **CORS errors**: Check the CORS configuration in `main.py`
2. **Token expiration**: Implement proper token refresh logic
3. **Invalid signatures**: Ensure the SECRET_KEY is consistent
4. **Import errors**: Make sure all dependencies are installed

### Debug Mode

The server runs with auto-reload enabled for development. Check the console output for detailed error messages.
