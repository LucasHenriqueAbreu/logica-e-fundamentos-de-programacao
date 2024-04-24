# Dicionários em Python

Os dicionários em Python são estruturas de dados poderosas que permitem armazenar pares de chave-valor de forma eficiente e flexível.

## Objetivo da Aula

- Compreender o conceito de dicionários em Python.
- Aprender a criar, acessar e manipular dicionários.
- Explorar operações e métodos comuns de dicionários.

## Conteúdo da Aula

### 1. O que são Dicionários?

Os dicionários são coleções desordenadas de pares de chave-valor. Cada chave é única e mapeia para um valor específico.

### 2. Sintaxe de Dicionários

A sintaxe básica para criar um dicionário em Python é usando chaves `{}` e especificando pares de chave-valor.

Exemplo:

```python
meu_dict = {"chave1": valor1, "chave2": valor2, "chave3": valor3}
```

### 3. Acesso a Elementos

Você pode acessar elementos em um dicionário utilizando suas chaves.

Exemplo:

```python
print(meu_dict["chave1"])  # Saída: valor1
```

### 4. Operações com Dicionários

Dicionários suportam várias operações, como adicionar, modificar, remover e verificar a existência de chaves.

Exemplos:

```python
meu_dict["chave1"] = novo_valor  # Atualiza o valor de uma chave existente
del meu_dict["chave2"]           # Remove uma chave do dicionário
existe_chave = "chave3" in meu_dict  # Verifica se a chave existe no dicionário
```

### 5. Iteração com Dicionários

Você pode iterar sobre chaves, valores ou itens de um dicionário usando loops `for` e métodos específicos.

Exemplo:

```python
for chave in meu_dict.keys():
    print(chave, meu_dict[chave])
```
