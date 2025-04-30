import axios from "axios";
import { FormEvent, useRef, useState } from "react";

interface CEP {
  logradouro: string,
  bairro: string,
  localidade: string,
}

export default function BuscarCEP() {
  const [cep, setCep] = useState<CEP | null>(null);
  const [erro, setErro] = useState(null);
  const [loading, setLoading] = useState(false);

  const formRef = useRef<HTMLFormElement>(null);

  function submit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);
    
    const cep = formRef.current?.querySelector("input")?.value;

    axios
      .get(`https://viacep.com.br/ws/${cep}/json/`)
      .then((res) => setCep(res.data))
      .catch((err) => setErro(err.message))
      .finally(() => setLoading(false));
  }

  return (
    <>
      <form ref={formRef} onSubmit={(e) => submit(e)}>
        <input type="text"></input>
        <button>Enviar</button>
      </form>
      {erro && <p>Erro: {erro}</p>}
      {loading && <p>Carregado...</p>}
      {cep && (
        <div>
          <p>Logradouro: {cep.logradouro}</p>
          <p>Bairro: {cep.bairro}</p>
          <p>Localidade: {cep.localidade}</p>
        </div>
      )}
    </>
  );
}
