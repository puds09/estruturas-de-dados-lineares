## Enunciado

<p>As crianças de Hawkins estão escondendo a verdade de Suzie – tendo em mente que a insanidade de suas vidas não faria o mínimo sentido para um forasteiro, portanto, eles inventam uma história na qual precisam de que ela contate um computador, de modo a rastrear um endereço de IP, que [seja lá por que razão] ajudaria os amigos a comprarem um novo videogame para Dustin. Apesar de desconfiada, por se tratar de Dustin, seu namorado, Suzie se depara com sua racionalidade fragilizada demais para quaisquer questionamentos, e usa suas habilidades em computação para – inconscientemente – infiltrar-se em um projeto ultra-secreto do governo e descobrir a localização de Eleven. Sendo grande fã da novelista Louisa May Alcott, Suzie se lembrou de que “são necessárias duas pedras para fazer fogo” e, sem mais delongas, contatou remotamente seu amigo programador, você, para ajudá-la a processar códigos de acesso que a possibilitariam manipular firewalls e o gerenciar a lista de redes confiáveis, garantindo-lhe a habilidade de se conectar ao endereço e, eventualmente, rastreá-lo. A sua tarefa se dará por meio de uma cadeia de processos que, ao serem executados, ajudarão Suzie a apagar seus rastros ou a obter chaves de dados criptografados, mas tenha cuidado: os processamentos se dão em uma ordem específica de prioridades, falta de cautela nessa gestão pode significar o fracasso da missão. Você deve, portanto, implementar as seguintes funções: </p>

<ul>
  <li>ENQUEUE X adiciona uma solicitação com X>0 processos à fila de execução. Este comando é seguido de X instâncias de solicitações para execução de um dos 2 comandos especiais listados a seguir. Toda solicitação inicia com uma valor inteiro 0≤P≤5
que determina sua prioridade, sendo valores menores os prioritários.
      <ul>
          <li>P scramble C para acobertar o processo, Suzie define a chave como um fluxo de símbolos alfanuméricos que é alterado com o uso de parênteses. Os caracteres são fornecidos numa sequência C, e a chave é definida pelo processamento das alterações definidas: o fluxo é deslocado para o início com o símbolo '(' ou para o ponto anterior a este deslocamento com ')'.</li>
          <li>P dekey O S com o intuito de remover ruídos para acobertar sua ação, a manipulação ocorre em endereços específicos de memória que são selecionados com a seguinte lógica: é fornecido um inteiro O indicando o número de operações a serem realizadas na sequência de inteiros S, que determinará o endereço de memória a ser manipulado. Cada operação envolve: (i) retirar 2 elementos do início da sequência (A e B) e, se A<B então adiciona A ao final da sequência S e B ao início; caso contrário adiciona A ao início da sequência S e B ao final. É garantido que há pelo menos 2 inteiros em S. Ao final, a função apresenta a junção de todos os números, determinando o novo endereço de memória a ser usado. É garantido que todo inteiro da sequência é positivo.</li>
      </ul>
  </li>
  <li>STOP interrompe a execução e mostra quantos comandos não foram executados.</li>
  <li>GO executa o próximo comando especial disponível na fila de processamento.</li>
</ul>



<p>A comunicação com o sistema é simples, as funcionalidades são apresentadas como descritas acima pelo sistema operacional, e seu programa deve organizá-las e executá-las.</p>

## Entrada
<p>A entrada consiste de uma série de comandos como os descritos. É garantido que o há pelo menos um comando stop</p>

## Saída
<p>A saída deve ser a informação resultante da execução de um comando especial ou stop, conforme especificados.</p>

#### Observações
<p>No segundo exemplo, são fornecidos os caracteres "Mensagem" e então se abre parênteses, o que implica que o fluxo é deslocado para o início da chave (antes dos caracteres já fornecidos). Quando é fornecido o outro parêntese, o deslocamento é para o fim da chave (que estaria configurada como "EisMensagem"). Os demais caracteres são acrescentados na ordem dada, determinando que a chave neste caso é "EisMensagemSecreta".</p>

![input-output](https://github.com/puds09/estruturas-de-dados-lineares/blob/main/input-output-examples.png)
