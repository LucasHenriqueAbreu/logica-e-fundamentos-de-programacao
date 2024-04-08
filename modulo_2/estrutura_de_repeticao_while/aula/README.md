# Estrutura de Repetição While em Python

## Objetivo da Aula
Compreender o funcionamento da estrutura de repetição `while`, seus usos e aplicabilidade em Python.

## Conteúdo da Aula

### Introdução

#### Analogia com Máquina de Café Automática

Vamos imaginar uma máquina de café automática que serve café para os clientes. A analogia com a estrutura de repetição `while` pode ser feita da seguinte forma:

- **Máquina de Café Automática:** A máquina representa a estrutura de repetição `while`. Ela executa uma série de passos para servir café até que uma condição seja atendida.

- **Condição de Repetição:** Suponha que a máquina continue servindo café enquanto houver xícaras disponíveis ou enquanto houver café no reservatório. Essa condição é verificada antes de cada ciclo de servir café.

- **Servir Café:** Cada vez que a máquina serve uma xícara de café, é como se uma iteração do `while` acontecesse. O processo continua até que a condição não seja mais atendida, ou seja, quando não há mais xícaras disponíveis ou café no reservatório.

### Exemplos de Código

Vamos ver alguns exemplos de uso do `while` em Python:

```python
# Exemplo 1: Contagem regressiva
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("Decolando!")

# Exemplo 2: Solicitação de entrada do usuário
resposta = ""
while resposta != "sair":
    resposta = input("Digite 'sair' para encerrar: ")
print("Programa encerrado.")
```

### Aplicações Práticas

- **Controle de Estoque:** Utilize o `while` para simular o controle de estoque de um produto, realizando pedidos enquanto houver demanda.

- **Validação de Entrada:** Crie um programa que solicita ao usuário uma senha até que ela seja digitada corretamente.

### Exercício

Escreva um programa Python que utilize a estrutura de repetição `while` para imprimir os números pares de 0 a 10.

```python
# Exercício: Imprimir números pares de 0 a 10
numero = 0
while numero <= 10:
    if numero % 2 == 0:
        print(numero)
    numero += 1
```

### Considerações Finais

O `while` é uma ferramenta poderosa para repetir ações enquanto uma condição é verdadeira, mas é necessário cuidado para evitar loops infinitos.
