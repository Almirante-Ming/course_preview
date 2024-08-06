const container=document.getElementById('container');



const url= "https://jsonplaceholder.typicode.com/comments";

async function getResponse(){
    const response = await fetch(url);
    const data= await response.json();
    
    data.map((post)=> {
        const divCard= document.createElement('div');
        divCard.classList.add("card");
        // const title=document.createElement('h1');
        // title.innerText=post.title
        const body=document.createElement('p');
        body.innerText=post.body
        const link=document.createElement('a');
        link.innerText="Retornar"
        link.setAttribute("href", "./index.html");

        // pesquisar sobre como pegar parametros de URL

        // divCard.appendChild(title);
        divCard.appendChild(body);
        divCard.appendChild(link);
        container.appendChild(divCard);
} )
 }


 getResponse();