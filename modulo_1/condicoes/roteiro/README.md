# Condições em Python

## Objetivo da Aula
Nesta aula, vamos explorar o uso de condições em Python para criar lógicas de decisão em programas. Vamos aprender sobre as estruturas `if`, `elif` e `else` e como utilizá-las para controlar o fluxo de execução do código.

## Agenda
1. Introdução às condições em Python
2. Utilização da estrutura `if`
3. Utilização das estruturas `elif` e `else`
4. Condições aninhadas
5. Exemplos práticos
6. Prática com exercícios
7. Próxima etapa

## Introdução às Condições em Python
As condições em Python permitem que você execute determinados blocos de código apenas se uma condição específica for atendida. Isso é fundamental para criar lógicas de decisão em seus programas.

## Utilização da Estrutura `if`
A estrutura de condição em Python é expressa usando a palavra-chave `if`. Aqui está como ela é usada:

```python
if condition:
    # código executado se condition for verdadeira
```

Agora, vamos ver um exemplo prático de como usar o `if`:

### Exemplo: Verificação de Idade
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
```

## Utilização das Estruturas `if` e `else`
As estruturas de condição em Python são expressas usando as palavras-chave `if`, como vimos antes e `else`. Aqui está como elas são usadas:

```python
if condition:
    # código executado se condition for verdadeira
else:
    # código executado se a condition for falsa
```

O bloco de código após o `else` é opcional e será executado apenas se a condição do `if` não for verdadeira.

### Exemplo: Verificação de Faixa Etária
```python
idade = 22

if idade < 18:
    print("Você é menor de idade.")
else:
    if idade < 60:
        print("Você é adulto.")
    else:
        print("Você é idoso.")
        
```

## Utilização das Estruturas `elif` e `else`
As estruturas de condição em Python também incluem as palavras-chave `elif` (abreviação de "else if") e `else`. Aqui está como elas são usadas:

```python
if condition:
    # código executado se condition for verdadeira
elif other_condition:
    # código executado se other_condition for verdadeira
else:
    # código executado se nenhuma das condições anteriores for verdadeira
```

Agora vamos explorar mais sobre o `elif` e `else`:

### Exemplo: Verificação de Nota
```python
nota = 75
if nota >= 90:
    print("Aprovado com distinção.")
elif nota >= 60:
    print("Aprovado.")
else:
    print("Reprovado.")
```

## Condições Aninhadas
Condições aninhadas referem-se à inclusão de uma estrutura `if` dentro de outra. Isso permite verificar várias condições em uma ordem específica.

```python
if condition1:
    # código executado se condition1 for verdadeira
    if condition2:
        # código executado se condition1 e condition2 forem verdadeiras
    else:
        # código executado se condition1 for verdadeira e condition2 for falsa
else:
    # código executado se condition1 for falsa
```

As condições aninhadas podem ser usadas para implementar lógicas complexas de decisão em seu programa.

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
- [Gabarito](../exercicios/GABARITO.md)

