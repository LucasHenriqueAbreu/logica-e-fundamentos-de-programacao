# Trabalho de Lógica e Fundamentos de Programação: Implementação do Jogo da Velha

## Descrição do Trabalho

Desenvolva um programa em python que implemente o clássico Jogo da Velha. O jogo deverá ser jogado por duas pessoas, alternando as jogadas entre os jogadores, sem necessidade de interação com a máquina.

## Regras do Jogo da Velha

1. **Objetivo:** O objetivo do jogo é conseguir alinhar três de seus símbolos (X ou O) em uma linha, coluna ou diagonal.
2. **Tabuleiro:** O tabuleiro é uma grade de 3x3, inicialmente vazia.
3. **Jogadores:** Dois jogadores participam do jogo, um utilizando o símbolo 'X' e o outro utilizando o símbolo 'O'.
4. **Jogadas:** Os jogadores se revezam para fazer suas jogadas. Em cada turno, um jogador escolhe uma das nove posições do tabuleiro que ainda não foi escolhida e marca essa posição com seu símbolo.
5. **Condições de Vitória:** O jogo termina quando um dos jogadores consegue alinhar três de seus símbolos em uma linha horizontal, vertical ou diagonal.
6. **Empate:** Se todas as nove posições do tabuleiro forem preenchidas e nenhum jogador tiver alinhado três símbolos, o jogo termina em empate.

## Requisitos

1. **Interface no Terminal:** O jogo deve ser totalmente jogável no terminal (linha de comando).
2. **Tabuleiro:** O tabuleiro do jogo deve ser exibido no terminal e atualizado após cada jogada.
3. **Alternância de Jogadores:** O jogo deve permitir que dois jogadores insiram suas jogadas alternadamente. Um jogador utilizará o símbolo 'X' e o outro jogador utilizará o símbolo 'O'.
4. **Verificação de Vitória:** O programa deve verificar após cada jogada se um dos jogadores venceu (três símbolos iguais em linha, coluna ou diagonal) ou se houve empate (tabuleiro completo sem vencedor).
5. **Mensagens Informativas:** O programa deve informar de quem é a vez de jogar, se houve uma jogada inválida (como tentar jogar em uma posição já ocupada), e deve anunciar o vencedor ou se houve empate quando o jogo terminar.

## Detalhamento das Funcionalidades

1. **Inicialização do Jogo:** Ao iniciar o jogo, o programa deve exibir um tabuleiro vazio e uma mensagem indicando qual jogador começará.
2. **Exibição do Tabuleiro:** O tabuleiro deve ser exibido em um formato claro e legível.
À medida que os jogadores fazem suas jogadas, o tabuleiro deve ser atualizado para refletir as posições ocupadas por 'X' e 'O'.
3. **Entrada do Usuário:** Solicite ao jogador atual que insira o número da posição onde deseja jogar. Caso a posição já esteja ocupada ou seja inválida, solicite a entrada novamente até que uma jogada válida seja feita.
4. **Verificação de Condições de Término:** Após cada jogada, o programa deve verificar se há um vencedor ou se o jogo terminou em empate. Se um jogador vencer, o programa deve anunciar o vencedor e encerrar o jogo. Se todas as posições estiverem ocupadas e não houver vencedor, o programa deve anunciar um empate.
5. **Reinício do Jogo:** Opcionalmente, após o término de um jogo, pergunte aos jogadores se desejam jogar novamente.

## Entrega

Em vez de entregar o código, cada aluno deverá fazer uma apresentação individual do projeto. Durante a apresentação, o aluno deve explicar claramente o que foi feito no projeto e como foi feito. Será avaliado o entendimento do código e do projeto. Caso fique claro que o aluno não desenvolveu o projeto por conta própria, o trabalho será zerado.

## Critérios de Avaliação

- **Funcionalidade Completa:** O jogo atende a todos os requisitos especificados.
- **Clareza e Legibilidade do Código:** Código bem organizado, comentado e fácil de entender.

Boa sorte e bom trabalho!


