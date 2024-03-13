# Exercícios

## 1. Verificar se um número é positivo, negativo ou zero:

```python
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
```

## 2. Verificar a faixa etária:

```python
idade = int(input("Digite a idade: "))

if idade < 18:
    print("Menor de idade.")
elif idade >= 18 and idade < 60:
    print("Maior de idade.")
else:
    print("Idoso.")
```

## 3. Determinar se um número é par ou ímpar:

```python
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

## 4. Encontrar o maior número entre três números:

```python
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior_numero = numero1

if numero2 > maior_numero:
    maior_numero = numero2
if numero3 > maior_numero:
    maior_numero = numero3

print("O maior número é:", maior_numero)
```

## 5. Verificar se um ano é bissexto ou não:

```python
ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
```

## 6. Classificar um aluno com base na sua nota:

```python
nota = float(input("Digite a nota do aluno: "))

if nota >= 9:
    print("Aprovado com distinção.")
elif nota >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")
```

## 7. Verificar se uma pessoa pode votar com base na sua idade:

```python
idade = int(input("Digite a idade: "))

if idade >= 16:
    print("Pode votar.")
else:
    print("Não pode votar.")
```

## 8. Verificar se três números podem formar os lados de um triângulo:

```python
a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

if a < b + c and b < a + c and c < a + b:
    print("Os números podem formar os lados de um triângulo.")
else:
    print("Os números não podem formar os lados de um triângulo.")
```

## 9. Determinar se uma pessoa pode se aposentar com base na sua idade e tempo de contribuição:

```python
idade = int(input("Digite a idade: "))
tempo_contribuicao = int(input("Digite o tempo de contribuição em anos: "))

if idade >= 65 or tempo_contribuicao >= 30 or (idade >= 60 and tempo_contribuicao >= 25):
    print("Pode se aposentar.")
else:
    print("Não pode se aposentar.")
```

## 10. Classificar um ano como "ano novo", "ano atual" ou "ano passado":

```python
ano = int(input("Digite o ano: "))

if ano > 2022:
    print("Ano novo.")
elif ano == 2022:
    print("Ano atual.")
else:
    print("Ano passado.")
```

## 12. Simular um sistema de login:

```python
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso.")
else:
    print("Usuário ou senha incorretos.")
```

## 13. Calcular o IMC (Índice de Massa Corporal) de uma pessoa:

```python
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Sobrepeso.")
else:
    print("Obeso.")
```

## 14. Verificar se um número é primo:

```python
numero = int(input("Digite um número: "))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print("O número não é primo.")
            break
    else:
        print("O número é primo.")
else:
    print("O número não é primo.")
```

## 15. Verificar se um ano é um ano de copa do mundo:

```python
ano = int(input("Digite o ano: "))

if (ano - 1930) % 4 == 0:
    print("É um ano de copa do mundo.")
else:
    print("Não é um ano de copa do mundo.")
```

## 16. Determinar se uma data é válida:

```python
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

valido = True

if mes < 1 or mes > 12:
    valido = False
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia < 1 or dia > 29:
            valido = False
    else:
        if dia < 1 or dia > 28:
            valido = False
elif mes in [4, 6, 9, 11]:
    if dia < 1 or dia > 30:
        valido = False
else:
    if dia < 1 or dia > 31:
        valido = False

if valido:
    print("Data válida.")
else:
    print("Data inválida.")
```

## 17. Classificar um triângulo com base no comprimento de seus lados:

```python
lado1 = float(input("Digite o comprimento do lado 1: "))
lado2 = float(input("Digite o comprimento do lado 2: "))
lado3 = float(input("Digite o comprimento do lado 3: "))

if lado1 == lado2 == lado3:
    print("Triângulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")
```

## 18. Verificar se um número é múltiplo de 3 e de 5 ao mesmo tempo:

```python
numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("O número é múltiplo de 3 e de 5 ao mesmo tempo.")
else:
    print("O número não é múltiplo de 3 e de 5 ao mesmo tempo.")
```

## 19. Determinar se um ano é bissexto ou não, considerando as regras do calendário gregoriano:

```python
ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
```

## 20. Calcular o desconto do INSS (Instituto Nacional do Seguro Social) de um funcionário com base no seu salário bruto:

```python
salario_bruto = float(input("Digite o salário bruto: "))

if salario_bruto <= 1100:
    desconto_inss = salario_bruto * 0.075
elif salario_bruto <= 2203.48:
    desconto_inss = salario_bruto * 0.09
elif salario_bruto <= 3305.22:
    desconto_inss = salario_bruto * 0.12
elif salario_bruto <= 6433.57:
    desconto_inss = salario_bruto * 0.14
else:
    desconto_inss = 751.99

print("Desconto do INSS:", desconto_inss)
```
