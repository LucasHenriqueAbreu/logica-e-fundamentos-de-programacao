# Condições em Python

## Objetivo da Aula
Nesta aula, vamos explorar o uso de condições em Python para criar lógicas de decisão em programas. Vamos aprender sobre as estruturas `if`, `elif` e `else` e como utilizá-las para controlar o fluxo de execução do código.

## Agenda
1. Introdução às condições em Python
2. Utilização das estruturas `if`, `elif` e `else`
3. Exemplos práticos
4. Prática com exercícios
5. Próxima etapa

## Introdução às Condições em Python
As condições em Python permitem que você execute determinados blocos de código apenas se uma condição específica for atendida. Isso é fundamental para criar lógicas de decisão em seus programas.

## Utilização das Estruturas `if`, `elif` e `else`
As estruturas de condição em Python são expressas usando as palavras-chave `if`, `elif` (abreviação de "else if") e `else`. Aqui está como elas são usadas:

- **if**: Verifica se uma condição é verdadeira e executa o bloco de código correspondente.
- **elif**: Verifica condições adicionais caso a condição inicial seja falsa.
- **else**: Executa o bloco de código se nenhuma das condições anteriores for verdadeira.

Exemplo de estrutura de condição em Python:

```python
if condition:
    # código executado se condition for verdadeira
elif other_condition:
    # código executado se other_condition for verdadeira
else:
    # código executado se nenhuma das condições anteriores for verdadeira
```

## Exemplos Práticos
Vamos explorar mais exemplos práticos para entender como as condições são utilizadas em Python.

### Exemplo 1: Verificação de Número Par
```python
numero = 7
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
```

### Exemplo 2: Verificação de Nota
```python
nota = 75
if nota >= 90:
    print("Aprovado com distinção.")
elif nota >= 60:
    print("Aprovado.")
else:
    print("Reprovado.")
```

### Exercício: Calculadora em Python

Desenvolva uma calculadora simples em Python que seja capaz de realizar as operações básicas de adição, subtração, multiplicação e divisão. Sua calculadora deve ser capaz de:

1. Receber como entrada dois números e a operação desejada.
2. Realizar a operação especificada nos dois números.
3. Exibir o resultado da operação.

Considere as seguintes especificações:

- A calculadora deve oferecer as opções para o usuário escolher a operação desejada (adição, subtração, multiplicação ou divisão).
- Após receber a entrada do usuário, a calculadora deve validar se a operação é válida.
- Para a operação de divisão, certifique-se de tratar casos de divisão por zero.
- O programa deve continuar rodando até que o usuário escolha sair.

Dica: Utilize estruturas de decisão (`if`, `elif`, `else`) para implementar a lógica da calculadora.

Teste sua calculadora com diferentes números e operações para garantir que ela está funcionando corretamente.

## Conclusão:
   - Recapitulação dos principais conceitos abordados na aula.
   - Encorajamento para que os alunos pratiquem programação em Python e explorem mais recursos disponíveis.

# Mais Exercícios
- [Exercícios](../exercicios/README.md) 

