# Introdução às Listas em Python

Nesta aula, vamos explorar o conceito de listas em Python, uma estrutura de dados versátil e fundamental na linguagem.

## Objetivo da Aula

- Compreender o que são listas em Python.
- Aprender a criar e manipular listas.
- Explorar as operações básicas de listas, como adição, remoção e ordenação de elementos.

## Conteúdo da Aula

1. **O que são listas?**
   - Explicação sobre listas como estruturas de dados ordenadas e mutáveis.
   - Comparação com outras estruturas de dados, como tuplas e conjuntos.

2. **Sintaxe de Listas**
   - Demonstrar a sintaxe de criação de listas usando colchetes `[ ]`.
   - Mostrar exemplos de listas com diferentes tipos de elementos.

   Exemplo:
   ```python
   minha_lista = [10, 20, 30, "abc", True]
   ```

3. **Acesso a Elementos**
   - Explicar como acessar elementos em uma lista usando índices.
   - Demonstração de acesso e modificação de elementos.

   Exemplo:
   ```python
   print(minha_lista[0])  # Saída: 10
   minha_lista[1] = 50    # Modifica o segundo elemento para 50
   ```

4. **Operações com Listas**
   - Adição de elementos usando `append()` e `insert()`.
   - Remoção de elementos com `remove()` e `pop()`.
   - Ordenação de listas com `sort()`.

   Exemplos:
   ```python
   minha_lista.append(40)     # Adiciona 40 ao final da lista
   minha_lista.remove("abc")  # Remove o elemento "abc"
   minha_lista.sort()         # Ordena a lista em ordem crescente
   ```

5. **Iteração com Listas**
   - Demonstração do uso de loops `for` para iterar sobre elementos de uma lista.
   - Utilização de listas em compreensões de listas (list comprehensions).

   Exemplo:
   ```python
   for item in minha_lista:
       print(item)
   ```

