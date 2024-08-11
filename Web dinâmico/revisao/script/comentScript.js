const container=document.getElementById('container');

const url= "https://jsonplaceholder.typicode.com/coments";
// const Comments = url.filter(comment => comment.postId == postId);

// async function getResponse(){
//     const response = await fetch(url);
//     const data= await response.json();
    
//     data.map((post)=> {
//         const divCard= document.createElement('div');
//         divCard.classList.add("card");
//         const title=document.createElement('h1');
//         title.innerText=post.title
//         const body=document.createElement('p');
//         body.innerText=post.body
//         const link=document.createElement('a');
//         link.innerText="retornar"
//         link.setAttribute("href", `https://jsonplaceholder.typicode.com/posts/${post.id}/comments`)
//         link.setAttribute("id", post.id )
    
//         divCard.appendChild(title);
//         divCard.appendChild(body);
//         divCard.appendChild(link);
//         container.appendChild(divCard);
        
//         console.log(post)
// } )
//  }


//  getResponse();


const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const postId = urlParams.get('postId');

// URL para buscar todos os comentários

async function getComments() {
    try {
        const response = await fetch(url);
        const comments = await response.json();

        // Filtra os comentários para exibir apenas aqueles com o postId correspondente
        const filteredComments = comments.filter(comment => comment.postId == postId);

        // Itera sobre os comentários filtrados e os exibe
        filteredComments.map((comment) => {
            const divCard = document.createElement('div');
            divCard.classList.add("card");

            const name = document.createElement('h3');
            name.innerText = comment.name;

            const body = document.createElement('p');
            body.innerText = comment.body;

            divCard.appendChild(name);
            divCard.appendChild(body);
            container.appendChild(divCard);
        });
    } catch (error) {
        console.error('Erro ao buscar comentários:', error);
    }
}

getComments();