/*let loadPosts = async () => {

}*/

/*async function loadPosts(){
    document.getElementById("posts").innerHTML = "Carregando..."

    let req = await fetch('https://jsonplaceholder.typicode.com/posts');
    let json = await req.json();

    montarBlog(json);

    /*fetch('https://jsonplaceholder.typicode.com/posts')
     .then(function(resultado){
         return resultado.json();
     })
      .then(function(json){
          montarBlog(json);
      })
      .catch(function(erro){
          console.log("Deu errado!");
      });
}*/

/*async function inserirPost(){
    document.getElementById("posts").innerHTML = "Carregando..."

    let req = await fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST', //o método GET não permite enviar informações no corpo da requisição
        body: JSON.stringify({
            title:'Titulo de teste',
            body:'Corpo de teste',
            userId: 4
        }),
        headers: {
            'Contente-Type': 'application/json'
        }
    });

    let json = await req.json();

    console.log(json);
};


function montarBlog(lista){
    
    let html = '';
    
    for (let i in lista) {
        
        html += '<h3>' + lista[i].title + '</h3>';
        html += lista[i].body+'<br/>';
        html += '<hr/>'
    }    
    
    document.getElementById("posts").innerHTML = html;
};

*/


/* FAZENDO UPLOAD DE ARQUIVO COM JS */

/*async function enviar(){
    let arquivo = document.getElementById("arquivo").files;

    let body = new FormData();
    body.append('title', 'Bla Bla Bla');
    body.append('arquivo', arquivo);

    let req = await fetch('https://www.meusite.com.br/upload',{
        method: 'POST',
        body: body,
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });

}*/

/* FAZENDO UPLOAD DE IMAGEM COM JS */

function mostrar(){
    let imagem = document.getElementById("imagem").files[0];

    let img = document.createElement("img");
    img.src = URL.createObjectURL(imagem);

    document.getElementById("area").appendChild(img)

    console.log(imagem)
}

/* USANDO O FILEREADER */

function mostrar(){
    let reader = new FileReader();
    let imagem = document.getElementById("imagem").files[0];

    reader.onloadend = function(){
        let img = document.createElement("img");
        img.src = reader.result;
        img.width = 200;

        document.getElementById("area").appendChild(img);
    }

    reader.readAsDataURL(imagem);
}



