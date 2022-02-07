"use strict";
let numero1 = document.getElementById('numero1');
let numero2 = document.getElementById('numero2');
let botao = document.getElementById('calcular');
let res = document.getElementById('resultado');
function calcular(n1, n2) {
    return n1 + n2;
}
botao.addEventListener('click', function () {
    res.innerHTML = calcular(+numero1.value, +numero2.value).toString(); //ou parseInt()
});
//let nomes: string[] = ['lucas', 'pedro', 'misael', 'raffael']
let nomes = ['lucas', 'pedro', 'misael', 'raffael'];
nomes.push(777);
let idades = [45, 61, 90, 25, 22];
// também podemos fazer assim let numeros: Array<number> = [45 ,99 ,78 ,96]
// types em funções:
function firstLetterUpperCase(name) {
    let firstLetter = name.charAt(0).toUpperCase();
    return firstLetter + name.substring(1);
}
//se eu quiser tipar o return...
/*function firstLetterUpperCase(name: string): string{
    let firstLetter = name.charAt(0).toUpperCase();
    return firstLetter + name.substring(1);
}*/
firstLetterUpperCase('lucas');
let names = ['lucas', 'pedro', 'misael', 'raffael'];
names.forEach(function (nome) {
    console.log(nome.toUpperCase());
});
//types em objetos
function resumo(usuario) {
    if (usuario.idade !== undefined) {
        return `Olá ${usuario.nome}, tudo bem? Você tem ${usuario.idade} anos`;
    }
    else {
        return `Olá ${usuario.nome}, tudo bem?`;
    }
}
let u = {
    nome: 'Lucas',
    sexo: 'Masculino',
    idade: 25
};
console.log(resumo(u));
//Union Types
// foi necessário fazer a verificação, pois o metodo uppercase não faria sentido em um numero
function mostrarIdade(idade) {
    if (typeof idade === 'string') {
        console.log(idade.toUpperCase());
    }
    else {
        console.log(idade);
    }
}
mostrarIdade(90);
mostrarIdade('90');
function apresentar(usuario) {
    return `Olá ${usuario.nome}, você tem ${usuario.idade} anos`;
}
apresentar({
    nome: 'Lucas',
    idade: 25
});
//type Assertions
let idadeField = document.getElementById('idade');
console.log(idadeField.value);
//types literals
//let nome: string = 'Lucas'; // se eu quiser aceitar somente um nome... aí..
let nome = 'Lucas';
nome = 'Lucas';
//nome = 'Pedro' // ele não deixa eu colocar outro valor para nome
//exemplo mais robusto
function mostrarTexto(texto, alinhamento) {
    return `<div style="text-align: ${alinhamento}">${texto}</div>`;
}
mostrarTexto('lucas', 'left');
mostrarTexto('lucas', 'right');
mostrarTexto('lucas', 'blablabla'); // e isso aqui não existe
function temNome(nome) {
    if (nome !== '') {
        return true;
    }
    else {
        return false;
    }
}
//inferencia literal
function fazerRequisicao(url, method) {
    //.......
}
let req = {
    url: 'https://alunos.b7web.com.br/',
    method: 'GET'
};
//let url = 'https://alunos.b7web.com.br/';
//let method: Methods = 'GET';
fazerRequisicao(req.url, req.method); //aqui o erro se dá pq eu simplesmente posso mudar a variável method. Então para solucionar eu posso criar um type
const somar = (n1, n2) => {
    return n1 + n2;
};
const subtrair = (n1, n2) => {
    return n1 - n2;
};
const multiplicar = (n1, n2) => {
    return n1 * n2;
};
const dividir = (n1, n2) => {
    return n1 / n2;
};
// Retorno void
function removerElemento(el) {
    el.remove();
}
removerElemento(document.getElementById('teste'));
//usando watchMode
