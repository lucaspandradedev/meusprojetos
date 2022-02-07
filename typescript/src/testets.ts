let numero1 = document.getElementById('numero1') as HTMLInputElement;
let numero2 = document.getElementById('numero2') as HTMLInputElement; 
let botao = document.getElementById('calcular');
let res = document.getElementById('resultado');


function calcular(n1: number, n2: number){
    return n1 + n2;
}


botao.addEventListener('click', function(){
    res.innerHTML = calcular( +numero1.value, +numero2.value ).toString(); //ou parseInt()
});


//let nomes: string[] = ['lucas', 'pedro', 'misael', 'raffael']

let nomes: any = ['lucas', 'pedro', 'misael', 'raffael']

nomes.push(777);

let idades: number[] = [45, 61, 90, 25, 22]

// também podemos fazer assim let numeros: Array<number> = [45 ,99 ,78 ,96]

// types em funções:

function firstLetterUpperCase(name: string){
    let firstLetter = name.charAt(0).toUpperCase();
    return firstLetter + name.substring(1);
}


//se eu quiser tipar o return...

/*function firstLetterUpperCase(name: string): string{
    let firstLetter = name.charAt(0).toUpperCase();
    return firstLetter + name.substring(1);
}*/

firstLetterUpperCase('lucas')



let names = ['lucas', 'pedro', 'misael', 'raffael']

names.forEach(function(nome){
    console.log(nome.toUpperCase());
});


//types em objetos

function resumo(usuario: {nome: string, idade?: number}){
    if(usuario.idade !== undefined){
        return `Olá ${usuario.nome}, tudo bem? Você tem ${usuario.idade} anos`
    } else{
        return `Olá ${usuario.nome}, tudo bem?`
    }
    
}

let u = {
    nome: 'Lucas',
    sexo: 'Masculino',
    idade: 25
};

console.log( resumo(u) )

//Union Types


// foi necessário fazer a verificação, pois o metodo uppercase não faria sentido em um numero
function mostrarIdade(idade: string | number) {
    if(typeof idade === 'string'){
        console.log(idade.toUpperCase())
    } else {
        console.log(idade);
    }    
}

mostrarIdade(90);
mostrarIdade('90')


// criando meu próprio type

/*type User = {
    nome: string,
    idade: number
};*/ // com o type eu não posso alterar as configurações do objeto

interface User {
    nome: string,
    idade: number
}

function apresentar(usuario){
    return `Olá ${usuario.nome}, você tem ${usuario.idade} anos`
}

apresentar({
    nome:'Lucas',
    idade: 25
})