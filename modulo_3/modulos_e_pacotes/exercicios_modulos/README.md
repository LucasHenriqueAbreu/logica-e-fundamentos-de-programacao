## Exercícios sobre Módulos e Pacotes em Python

### Exercício 1: Criando um Módulo Simples
Crie um módulo chamado `matematica.py` que contenha duas funções: `soma(a, b)` que retorna a soma de dois números e `subtracao(a, b)` que retorna a diferença entre dois números. Em seguida, crie um script que importe este módulo e use suas funções.

### Exercício 2: Usando Funções de um Módulo
Crie um módulo chamado `saudacoes.py` com uma função `cumprimentar(nome)` que imprime uma saudação personalizada. Importe este módulo em outro script e chame a função `cumprimentar` com diferentes nomes.

### Exercício 3: Importando Partes Específicas de um Módulo
Altere o exercício 1 para importar apenas a função `soma` do módulo `matematica.py` e utilize-a em um script. Não importe a função `subtracao`.

### Exercício 4: Pacote com Múltiplos Módulos
Crie um pacote chamado `geometria` com dois módulos: `retangulo.py` e `circulo.py`. No módulo `retangulo.py`, crie funções para calcular a área e o perímetro de um retângulo. No módulo `circulo.py`, crie funções para calcular a área e a circunferência de um círculo. Crie um script que importe esses módulos e use suas funções.

### Exercício 5: Inicialização de Pacote
Adicione um arquivo `__init__.py` no pacote `geometria` criado no exercício 4. No arquivo `__init__.py`, importe todas as funções dos módulos `retangulo.py` e `circulo.py`. Teste a importação das funções diretamente do pacote `geometria`.

### Exercício 6: Importação Ponto a Ponto
Usando o pacote `geometria` do exercício 4, escreva um script que utilize importações ponto a ponto (por exemplo, `import geometria.retangulo`, `import geometria.circulo`). Use as funções dos módulos importados para calcular a área de um retângulo e a área de um círculo.

### Exercício 7: Função de Inicialização no `__init__.py`
No arquivo `__init__.py` do pacote `geometria`, adicione uma função `bem_vindo()` que imprime uma mensagem de boas-vindas ao pacote `geometria`. Importe e chame esta função em um script separado.

### Exercício 8: Utilizando Variáveis Globais
Crie um módulo chamado `configuracoes.py` que contenha variáveis globais como `tamanho_tela`, `cor_fundo`, etc. Em um script separado, importe e modifique essas variáveis globais.

### Exercício 9: Reutilizando Módulos em Diferentes Scripts
Crie um módulo chamado `utilitarios.py` que contenha funções úteis como `ler_arquivo(caminho)`, `escrever_arquivo(caminho, conteudo)`, etc. Crie dois scripts separados que utilizem essas funções para ler e escrever arquivos.

### Exercício 10: Pacote com Subpacotes
Crie um pacote chamado `empresa` com um subpacote chamado `departamentos`. Dentro do subpacote `departamentos`, crie dois módulos: `financeiro.py` e `rh.py`. No módulo `financeiro.py`, crie funções relacionadas a finanças (ex: `calcular_salario()`). No módulo `rh.py`, crie funções relacionadas a recursos humanos (ex: `contratar_funcionario()`). Crie um script que importe e use funções de ambos os módulos.
