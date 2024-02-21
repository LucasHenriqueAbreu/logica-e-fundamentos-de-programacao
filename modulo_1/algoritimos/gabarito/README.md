### Gabarito dos Exercícios sobre Algoritmos:

#### I. Problemas Básicos
1. **Calcular a Média de Três Números:**
   - Algoritmo:
     - Receba três números como entrada (num1, num2, num3).
     - Calcule a média aritmética dos números: média = (num1 + num2 + num3) / 3.
     - Exiba a média calculada.

2. **Determinar o Maior de Dois Números:**
   - Algoritmo:
     - Receba dois números como entrada (num1, num2).
     - Verifique se num1 é maior que num2.
       - Se sim, exiba num1 como o maior número.
       - Caso contrário, exiba num2 como o maior número.

3. **Verificar se um Número é Positivo, Negativo ou Zero:**
   - Algoritmo:
     - Receba um número como entrada (num).
     - Verifique se num é maior que zero.
       - Se sim, exiba "O número é positivo".
       - Se num é igual a zero, exiba "O número é zero".
       - Caso contrário, exiba "O número é negativo".

#### II. Problemas Intermediários
4. **Verificar se um Número é Primo:**
   - Algoritmo:
     - Receba um número como entrada (num).
     - Inicialize uma variável para contar divisores (divisores = 0).
     - Para cada número de 1 a num, verifique se num é divisível por ele.
       - Se sim, incremente o contador de divisores.
     - Se divisores for igual a 2, exiba "O número é primo".
       - Caso contrário, exiba "O número não é primo".

5. **Calcular a Área de um Triângulo:**
   - Algoritmo:
     - Receba os comprimentos dos três lados do triângulo como entrada (lado1, lado2, lado3).
     - Use a fórmula de Herão para calcular a área do triângulo:
       - semi_perímetro = (lado1 + lado2 + lado3) / 2
       - área = √(semi_perímetro * (semi_perímetro - lado1) * (semi_perímetro - lado2) * (semi_perímetro - lado3))
     - Exiba a área calculada.

6. **Determinar se um Número é Divisível por Outro Número:**
   - Algoritmo:
     - Receba dois números como entrada (num, divisor).
     - Verifique se num é divisível por divisor.
       - Se o resto da divisão de num por divisor for igual a zero, exiba "O número é divisível pelo divisor".
       - Caso contrário, exiba "O número não é divisível pelo divisor".

#### III. Problemas Avançados
7. **Converter uma Temperatura de Celsius para Fahrenheit:**
   - Algoritmo:
     - Receba a temperatura em Celsius como entrada (temp_celsius).
     - Converta a temperatura para Fahrenheit usando a fórmula: temp_fahrenheit = (temp_celsius * 9/5) + 32.
     - Exiba a temperatura em Fahrenheit.

8. **Verificar se uma String é um Palíndromo:**
   - Algoritmo:
     - Receba uma string como entrada (texto).
     - Inverta a string.
     - Verifique se a string invertida é igual à string original.
       - Se sim, exiba "A string é um palíndromo".
       - Caso contrário, exiba "A string não é um palíndromo".

9. **Calcular o Fatorial de um Número:**
   - Algoritmo:
     - Receba um número como entrada (num).
     - Inicialize uma variável para armazenar o resultado do fatorial (fatorial = 1).
     - Para cada número de 1 a num, multiplique o fatorial pelo número atual.
     - Exiba o fatorial calculado.

10. **Ordenar um Conjunto de Números em Ordem Crescente:**
    - Algoritmo:
      - Receba um conjunto de números como entrada.
      - Ordene os números em ordem crescente.
      - Exiba os números ordenados.
