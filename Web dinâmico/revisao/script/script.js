const container=document.getElementById('container');



const url= "https://jsonplaceholder.typicode.com/posts";

async function getResponse(){
    const response = await fetch(url);
    const data= await response.json();
    
    data.map((post)=> {
        const divCard= document.createElement('div');
        divCard.classList.add("card");
        const title=document.createElement('h1');
        title.innerText=post.title
        const body=document.createElement('p');
        body.innerText=post.body
        const link=document.createElement('a');
        link.innerText="ler mais..."
        link.setAttribute("href", `https://jsonplaceholder.typicode.com/posts/${post.id}/comments`)
        link.setAttribute("id", post.id )
    
        divCard.appendChild(title);
        divCard.appendChild(body);
        divCard.appendChild(link);
        container.appendChild(divCard);
        
        console.log(post)
} )
 }


 getResponse();

//Atividade: ao clicar no leia mais... abrir outra pagina com as informações dos comentarios de cada post pelo id, apresentar nome, email e o comentario.
//link para usar: https://jsonplaceholder.typicode.com/comments?postId=1 se substituir o 1 ali no final aparece os outros posts.
// como pegar um atributo da url com javascript?