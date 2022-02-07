import {Header} from './components/Header';
import {Photo} from './components/Photo';
import {useState} from 'react';

/*const acaoBotao = () => {
  alert("O botão foi clicado!");
}*/

//Como eu só exportei a componente ''olaMundo'', então tenho que jogar meu header lá
/*const olaMundo = () => {
  return (
    <div>
      <Header title="Este é um exemplo"/>
      <Header title="Um outro título"/> 
      Olá, mundo!

      <Photo url="https://revistanossa.com.br/midias/artigos/Imagens/new-google-favicon-logo-1607949797.png" legend="Google"/>

      <button onClick={acaoBotao}>Clique aqui para confirmar</button>
    </div>
  );
}*/
//também posso executar a funcão direto na prop do meu botão
//export default olaMundo;

/*const contador = () => {
  
  let [nu, setNumber] = useState(0);

  var adicionar = () => {
    setNumber(nu += 1);
  }

  var subTrair = () => {
    setNumber(nu -= 1);
  }
  
  return (
    <div>
      <button onClick={adicionar}>+</button>
      -- ({nu}) --
      <button onClick={subTrair}>-</button>
    </div>
  );
};

export default contador;
*/

const form = () => {
  const [nome, setNome] = useState('')

  const valor = (event: React.FormEvent<HTMLInputElement>) => {
    setNome( (event.target as HTMLInputElement).value )
  }
  return (
    <div>
      Nome:
      <input type="text" value={nome} onChange={valor} />
      <hr />
      Seu nome é: {nome}
    </div>
  )
}

export default form;