# Desafio Técnico: Sistema de Folha de Pagamento – Versão Simplificada

## Contexto

Você foi contratado como **desenvolvedor Python júnior** em uma pequena empresa de software que atende escritórios de contabilidade e RH. Seu líder de equipe te passou a primeira tarefa com a seguinte explicação:

> “A gente precisa de um sisteminha simples, feito só com Python, que simule a folha de pagamento dos funcionários. Não precisa usar banco de dados, nem criar tela. Só rodar no terminal mesmo. A ideia é termos um programa que cadastre os funcionários e gere a folha mensal com base em regras simples de desconto.”

---

## Requisitos do Sistema

### 1. **Cadastro de Funcionários**

O sistema deve permitir que o usuário cadastre manualmente os seguintes dados:

- Nome do funcionário
- Cargo
- Salário bruto mensal (valor numérico)

Esses dados devem ser armazenados em uma **estrutura adequada em memória**, como uma **lista de dicionários**.

---

### 2. **Listagem de Funcionários**

O usuário deve conseguir listar todos os funcionários cadastrados, com as seguintes informações:

- Nome
- Cargo
- Salário bruto

---

### 3. **Geração da Folha de Pagamento**

Para cada funcionário cadastrado, o sistema deve calcular:

- **INSS**: 11% sobre o salário bruto
- **FGTS**: 8% sobre o salário bruto (apenas mostrado, não descontado do salário)
- **Salário líquido**: salário bruto menos o desconto do INSS

Ao exibir a folha de pagamento, mostre claramente:

```
Nome: João da Silva
Cargo: Analista de Sistemas
Salário Bruto: R$ 3.000,00
INSS (11%): R$ 330,00
FGTS (8%): R$ 240,00
Salário Líquido: R$ 2.670,00
```

---

### 4. **Menu de Navegação**

O sistema deve exibir um menu no terminal com as seguintes opções:

1. Cadastrar funcionário  
2. Listar funcionários  
3. Gerar folha de pagamento  
4. Sair

O usuário deve conseguir executar várias ações até decidir sair do programa.

---

## Regras de Negócio

- O sistema deve aceitar o cadastro de **vários funcionários**.
- Os valores devem ser sempre mostrados com **duas casas decimais**.
- Nenhum valor deve ser negativo ou inválido.
- O salário líquido deve considerar **somente o desconto do INSS**.

---

## Objetivo do Desafio

O desafio visa praticar:

- Manipulação de listas e dicionários
- Entrada e saída de dados com `input()` e `print()`
- Uso de funções para organizar o código
- Operações matemáticas
- Estrutura de repetição e menus
