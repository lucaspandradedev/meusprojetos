/*let lista1 = [0, 5, 3, 11, 9, 15]
lista1.sort((a, b) => a - b)
console.log(lista1)*/

/*let lista = document.getElementById('novomenu');
let novoitem = document.createElement('li');
novoitem.appendChild(document.createTextNode('OLHA EU AQUIIII'))
lista.appendChild(novoitem)*/

/*window.onload = function() {
    document.getElementById('cabeça').innerHTML = "ooomiiiiiiiiiiiiiiiii";
    alert('Opa, tudo bom amigão?');
    document.querySelector('#cabeça').classList.add('mudazul');
}*/

/*function mostrarTelefone(){
    document.querySelector('#telefone').style.display = 'block';
    document.querySelector('.show--button').style.display = 'none';
}*/

/*let html = '';

let c = 0;

while (c < 10) {
    html ++ "Número: "+c+"<br/>";
    c++;

}

document.querySelector('.demo').innerHTML = html;
*/

/*let n = 10;

num = n.toString();

console.log(num);*/


/*let lista = ["Ovo", "Farinha", "Leite", "Margarina"]

let res = lista.splice(1,2)

console.log(lista)
console.log('Depois de alterada: '+ lista)*/


//se eu tivesse uma segunda lista, poderia usar o .concat para juntar

/*let timer; 

function comecar(){
    timer = setInterval(showTime);
}

function parar(){
    clearInterval(timer);
}


function showTime(){
    let d = new Date();
    let h = d.getHours();
    let m = d.getMinutes();
    let s = d.getSeconds();
    let txt = h+':'+m+':'+s;

    document.querySelector('.demo').innerHTML = txt
}
*/


/*let timer;

function rodar(){
    timer = setTimeout(function(){
        document.querySelector('.demo').innerHTML = 'Rodoou!    '
    }, 2000)
}

function parar(){
    clearTimeout(timer);
}*/


let pessoa = {
    nome: 'Lucas',
    sobrenome: 'Pereira',
    idade: 25,
    social: {
        facebook: 'lucaspereira',
        instagram: '@lpdas_',
        github: '@lucaspandradedev'
    },
    nomeCompleto: function() {
        return `${this.nome} ${this.sobrenome}`;
    }
};

let {nome:nomedomeliante, sobrenome, idade} = pessoa

console.log(nomedomeliante, sobrenome, idade);

