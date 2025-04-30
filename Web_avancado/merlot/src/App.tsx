import {useState, FormEvent, useRef } from 'react';
import {Style} from '@/style/form'
import {Form, FormLabel}   from '@/components/ui/form';
// import axios from 'axios';

interface payload {
  username: string;
  password: string;
}



export default function App() {

  const [loading, setLoading] = useState(false);
  // const [err, setErr] = useState(null);

  const formRef = useRef<HTMLFormElement>(null);



  function submit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);
    
    let Payload: payload = {
      username: formRef.current?.querySelector("#user")?.value,
      password: formRef.current?.querySelector("#pass")?.value
    };
    

     setLoading(false);
    console.log(Payload);


  };

  return (
    <>
      <h1>Login Page</h1>
      <form ref={formRef} onSubmit={(e) => submit(e)} style={Style.form}>
        <input type="text" placeholder="Username" id='user' />
        <input type="password" placeholder="Password" id='pass'/>
        <button>Login</button>
        {loading && <p>Loading...</p>}
        {/* {err && <p>Error: {err}</p>} */}
      </form>   
    </>
  )
}

