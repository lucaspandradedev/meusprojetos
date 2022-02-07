type Props = {
    title?: string;
}


export const Header = ({ title }: Props) => {
    return(
      <header>
        <h1>{title}</h1>
        <hr />
      </header>
    )
  }

//posso escrever assim também
/*export const Header = (props: Props) => {
    return(
      <header>
        <h1>{props.title}</h1>
        <hr />
      </header>
    )
  }*/
