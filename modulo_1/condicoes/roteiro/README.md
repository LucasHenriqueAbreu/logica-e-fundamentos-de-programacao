# Condições em Python

## Objetivo da Aula
Nesta aula, vamos explorar o uso de condições em Python para criar lógicas de decisão em programas. Vamos aprender sobre as estruturas `if`, `elif` e `else` e como utilizá-las para controlar o fluxo de execução do código.

## Agenda
1. Relebrar o tipo primitivo boolean
2. Conectivos lógicos
3. Operadores de comparação
4. Introdução às condições em Python
5. Utilização da estrutura `if`
6. Utilização das estruturas `elif` e `else`
7. Condições aninhadas
8. Exemplos práticos
9. Prática com exercícios
10. Próxima etapa

## Relembrando o Tipo Primitivo Booleano

O tipo primitivo booleano em Python, `bool`, representa um valor de verdade. Ele pode ter dois valores: `True` ou `False`. Esses valores são frequentemente usados em expressões lógicas e condições.

Exemplo:
```python
verdadeiro = True
falso = False
print(verdadeiro)  # Saída: True
print(falso)       # Saída: False
```

## Conectivos Lógicos

Os conectivos lógicos em Python são utilizados para combinar ou modificar valores booleanos. Os principais conectivos são `and` e `or`.

### Operador `and`

O operador `and` retorna `True` se ambas as expressões forem verdadeiras, caso contrário, retorna `False`.

Exemplo:
```python
expressao1 = True
expressao2 = False
resultado = expressao1 and expressao2
print(resultado)  # Saída: False
```

### Operador `or`

O operador `or` retorna `True` se pelo menos uma das expressões for verdadeira, caso contrário, retorna `False`.

Exemplo:
```python
expressao1 = True
expressao2 = False
resultado = expressao1 or expressao2
print(resultado)  # Saída: True
```

## Operadores de Comparação

Os operadores de comparação são utilizados para comparar dois valores e retornar um valor booleano. Os principais operadores são: `>`, `<`, `>=`, `<=`, `==`, `!=`.

### Operador `>`

O operador `>` verifica se o valor da esquerda é maior que o valor da direita.

Exemplo:
```python
x = 5
y = 3
resultado = x > y
print(resultado)  # Saída: True
```

### Operador `>=`

O operador `>=` verifica se o valor da esquerda é maior ou igual ao valor da direita.

Exemplo:
```python
x = 5
y = 5
resultado = x >= y
print(resultado)  # Saída: True
```

### Operador `<`

O operador `<` verifica se o valor da esquerda é menor que o valor da direita.

Exemplo:
```python
x = 3
y = 5
resultado = x < y
print(resultado)  # Saída: True
```

### Operador `<=`

O operador `<=` verifica se o valor da esquerda é menor ou igual ao valor da direita.

Exemplo:
```python
x = 5
y = 5
resultado = x <= y
print(resultado)  # Saída: True
```

### Operador `==`

O operador `==` verifica se os valores dos dois operandos são iguais.

Exemplo:
```python
x = 5
y = 5
resultado = x == y
print(resultado)  # Saída: True
```

### Operador `!=`

O operador `!=` verifica se os valores dos dois operandos são diferentes.

Exemplo:
```python
x = 5
y = 3
resultado = x != y
print(resultado)  # Saída: True
```

## Uso do `if`

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

## Uso do `if` com `else`

A estrutura de condição em Python também pode incluir a palavra-chave `else`. Aqui está como ela é usada:

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
    print("Você é adulto.")
```

## Uso do `if`, `elif` e `else`

A estrutura de condição em Python também inclui as palavras-chave `elif` (abreviação de "else if") e `else`. Aqui está como elas são usadas:

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

