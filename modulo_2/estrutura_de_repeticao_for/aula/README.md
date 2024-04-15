# Roteiro de Aula - Estruturas de Repetição "for" em Python

## Introdução
Nesta aula, vamos explorar a estrutura de repetição "for" em Python. O "for" é usado para iterar sobre sequências de elementos, como strings, listas, tuplas ou até mesmo sequências numéricas geradas pela função `range()`.

## Descrição
O "for" em Python é uma estrutura de controle de fluxo que permite executar um bloco de código várias vezes, uma para cada item na sequência especificada. Ele simplifica a iteração sobre elementos e é muito útil em muitos cenários de programação.

## Objetivos
- Entender o funcionamento básico da estrutura de repetição "for" em Python.
- Aprender a usar a função `range()` para gerar sequências numéricas.
- Praticar com exemplos de código para consolidar o aprendizado.

## Exemplos de Código

### Exemplo 1: Iteração sobre uma sequência de números
```python
for num in range(1, 6):
    print(num)
```

### Exemplo 2: Iteração sobre uma string
```python
frase = "Python é incrível!"
for letra in frase:
    print(letra)
```

### Exemplo 3: Iteração sobre uma lista
```python
numeros = [10, 20, 30, 40, 50]
soma = 0
for num in numeros:
    soma += num
print("Soma dos números:", soma)
```

## Conclusão
A estrutura de repetição "for" é uma ferramenta poderosa para iterar sobre sequências em Python. Combinada com a função `range()`, podemos criar iterações precisas e eficientes em nossos programas.
