/*desconstrução de arrays*/

/*let info = ['Bonieky Lacerda', 'Bonieky', 'Lacerda', '@bonieky'];

let [nomeCompleto, nome, sobrenome, instragram] = info; // posso também deixar algumas variáveis em branco para "pular intens que não queremos pegar"

console.log(nomeCompleto, nome, sobrenome, instragram);*/


/*arrows functions*/

/*let somar = (x, y) => {
    return x+y;
} se eu colocar as chaves, tenho que usar o return*/

//posso fazer também assim:

let somar = (x, y) => x + y;

// let letrasNome = nome => nome.length; **isso é mais recomendando quando se tem apenas um parâmetro

console.log(somar(10, 5));

/*Operador SPREAD*/

let numeros = [1,2,3,4,5,6];

let outros = [...numeros, 7,8,9,10]

console.log(outros)

let info = {
    nome: 'Bonieky',
    sobrenome: 'Lacerda',
    idade: 99
};


let maisInfo = { 
    ...info,
    cidade: 'Natal',
    pais: 'Brasil'
}; //pode ser feito com função também

console.log(info)
console.log(maisInfo)


/*operador REST*/

function adicionar(...numeros){

    console.log(numeros);
}

adicionar(5,6,7,8,9,10)

/*INCLUDES E REPEAT*/

let list = ['café', 'arroz','feijão','açucar'];

console.log(list.includes('café'));

let nome = 'Bonieky';

console.log(nome.includes('a'))

/*OBJECTS KEYS, VALUES E ENTRIES*/

let lista = ['café', 'arroz','feijão','açucar'];

console.log(Object.entries(lista))

let pessoa = {
    nome: 'Lucas',
    sobrenome: 'Pereira',
    idade: 25
};

console.log(Object.keys(pessoa));

/* String, padStart, padEnd */

let telefone = '5';

console.log(telefone.padEnd(9, 'x'));

let cartao = '1234 5678 8898 9654';

let lastDigi = cartao.slice(-4)

let cartaomascarado = lastDigi.padStart(16, '*')

// console.log(`Este é o seu cartão? ${cartao}`)

console.log(`Os quatro últimos dígitos do seu cartão são ${cartaomascarado}?`)

/*JSON*/

JSON.stringify({nome: 'Lucas', idade: 25, sexo: 'Masculino'})

/* PROMISES */

// AQUI O PROFESSOR CRIOU A PROMESSA
function pegarTemperatura(){
    return new Promise(function(resolve, reject){
        console.log("Pegando temperatura...");

        setTimeout(function(){
            resolve('40 na sombra');
        }, 2000);
    });
}

//USANDO A PROMISA

let temp = pegarTemperatura();
temp.then(function(resultado){
    console.log("TEMPERATURA: "+ resultado)
});



