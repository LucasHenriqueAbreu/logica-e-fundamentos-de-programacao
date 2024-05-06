# Roteiro de Aula: Introdução às Funções em Python

## Objetivo da Aula:
- Compreender o conceito de funções em Python.
- Aprender a criar funções simples e funções com parâmetros.
- Entender o uso de funções para organizar e reutilizar código.

## 1. Introdução
Nesta aula, vamos aprender sobre funções em Python. As funções são blocos de código que realizam tarefas específicas e podem ser reutilizadas ao longo do programa. Elas ajudam a organizar o código e melhorar a manutenção do programa.

## 2. O que são Funções?
Funções em Python são definidas usando a palavra-chave `def` seguida do nome da função e dos parênteses `()`. Podemos criar funções simples que executam tarefas específicas.

```python
def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()  # Chamando a função para exibir a saudação
```

## 3. Criando Funções Simples
Vamos criar uma função que calcula a soma de dois números e exibe o resultado.

```python
def soma(a, b):
    resultado = a + b
    print(f"A soma de {a} e {b} é {resultado}")

soma(5, 3)  # Chamando a função para calcular a soma
```

## 4. Parâmetros e Retorno de Funções
As funções podem receber parâmetros e retornar valores calculados. Vamos criar uma função que calcula o quadrado de um número e retorna o resultado.

```python
def quadrado(numero):
    return numero ** 2

resultado = quadrado(4)  # Chamando a função para calcular o quadrado de 4
print(f"O quadrado de 4 é {resultado}")
```

## 5. Escopo de Variáveis
Em Python, variáveis têm escopo local dentro de uma função, a menos que sejam declaradas como globais. Variáveis locais só existem dentro da função onde são definidas.

```python
def exemplo_escopo():
    variavel_local = 10  # Variável local dentro da função
    print(f"Variável local: {variavel_local}")

exemplo_escopo()
# print(variavel_local)  # Isso resultaria em um erro, pois a variável local não é acessível fora da função
```

## 6. Exercício Prático
Vamos propor um exercício onde os alunos devem criar uma função que recebe uma lista de números e retorna a soma desses números.

```python
def soma_lista(numeros):
    total = sum(numeros)
    return total

lista_numeros = [1, 2, 3, 4, 5]
resultado_soma = soma_lista(lista_numeros)
print(f"A soma dos números na lista é {resultado_soma}")
```

## 7. Funções com Argumentos Padrão
Podemos definir argumentos padrão em funções, facilitando seu uso em diferentes situações.

```python
def saudacao_personalizada(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao_personalizada("Maria")  # Exibe: Olá, Maria!
saudacao_personalizada("João", "Oi")  # Exibe: Oi, João!
```

## 8. Documentando Funções
É importante documentar funções usando docstrings para descrever seu propósito e funcionamento.

```python
def soma(a, b):
    """
    Esta função calcula a soma de dois números.

    Args:
    a (int): O primeiro número.
    b (int): O segundo número.

    Returns:
    int: A soma dos dois números.
    """
    return a + b
```

## 9. Conclusão e Exercício de Fixação
Recapitule os principais pontos abordados na aula e proponha aos alunos um exercício para criar uma série de funções para resolver um problema específico, como manipulação de listas, cálculos matemáticos, etc.

## 10. Perguntas e Respostas
Abra espaço para perguntas dos alunos sobre funções em Python e esclareça dúvidas.
