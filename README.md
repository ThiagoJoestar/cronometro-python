# Cronômetro em Python com Programação Orientada a Objetos

Este é um cronômetro simples em Python, implementado usando Programação Orientada a Objetos (POO).

## Classe `Cronometro`

A classe `Cronometro` representa um cronômetro com contagem de horas, minutos, segundos e milésimos.

### Método `__init__(self, milesimos=0, segundos=0, minutos=0, horas=0)`

Construtor da classe `Cronometro`: Inicializa as variáveis de instância com valores padrão.

- **Parâmetros:**
  - `milesimos`: Valor inicial dos milésimos de segundo.
  - `segundos`: Valor inicial dos segundos.
  - `minutos`: Valor inicial dos minutos.
  - `horas`: Valor inicial das horas.

### Método `__repr__(self)`

Método especial que retorna uma representação formatada em string do tempo no formato HH:MM:SS:mm.

- **Retorno:**
  - String formatada representando o tempo atual.

### Método `incremento(self)`

Incrementa os milésimos de segundo e atualiza os segundos, minutos e horas conforme necessário.

### Método `start(self)`

O método `start` é responsável por iniciar o cronômetro em um loop infinito, atualizando e exibindo o tempo a cada 0.1 segundo. Utiliza as funções `os.system` para limpar a tela e `time.sleep` para pausar a execução e criar o efeito de contagem contínua.

- **Funcionamento:**

  **Loop Infinito:**
     - O método entra em um loop que continuará indefinidamente.
   
   **Atualização do Tempo:**
     - A cada iteração do loop, o método chama a função `incremento`, que atualiza os milésimos, segundos, minutos e horas do cronômetro.
   
   **Limpeza da Tela:**
     - Utiliza `os.system` para limpar a tela, proporcionando uma exibição contínua do tempo.
     - É ultilizado o comando 'cls' para limpar a tela, esse comando é valido somente em sistemas Windows, para sistemas Linux / Unix deve ser ultilizado o comando 'clear' para a limpeza do terminal.
   
   **Exibição do Tempo:**
     - Imprime a representação formatada do tempo usando o método `__repr__`, que mostra horas, minutos, segundos e milésimos.
   
   **Pausa:**
     - Pausa a execução por 0.1 segundo usando `time.sleep` para criar um intervalo de atualização visível.

O método `start` permite que o cronômetro funcione de forma contínua, proporcionando uma representação visual precisa do tempo decorrido.


