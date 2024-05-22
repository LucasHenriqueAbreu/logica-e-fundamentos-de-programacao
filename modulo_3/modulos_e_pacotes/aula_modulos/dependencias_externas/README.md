# Aula sobre Pacotes Externos e Ambientes Virtuais em Python

## Pacotes Externos em Python

### O que são Pacotes Externos?

Pacotes externos são bibliotecas ou módulos desenvolvidos por terceiros que não estão incluídos na biblioteca padrão do Python. Eles oferecem funcionalidades adicionais que podem ser facilmente incorporadas aos seus projetos.

### Instalando Pacotes Externos

Para instalar um pacote externo, você pode usar o gerenciador de pacotes `pip`, que é incluído por padrão na maioria das instalações do Python. Basta executar o seguinte comando no terminal:

```bash
pip install nome_do_pacote
```

Isso instalará o pacote especificado e suas dependências, se houver, no seu ambiente Python.

### Usando Pacotes Externos

Depois de instalar um pacote externo, você pode usá-lo em seus scripts Python. Basta importar o pacote da mesma forma que você importaria um módulo interno:

```python
import nome_do_pacote

# Use as funcionalidades do pacote externo aqui
```

## Ambientes Virtuais em Python

### O que são Ambientes Virtuais?

Ambientes virtuais são ambientes Python isolados que permitem gerenciar dependências e pacotes para projetos específicos. Eles permitem que você tenha diferentes versões de pacotes instalados em diferentes projetos, evitando conflitos entre as dependências.

### Criando um Ambiente Virtual com `venv`

O módulo `venv` é uma ferramenta Python integrada que permite criar e gerenciar ambientes virtuais. Aqui está como criar um ambiente virtual usando `venv`:

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório do seu projeto.
3. Execute o seguinte comando para criar um novo ambiente virtual:

```bash
python -m venv nome_do_ambiente
```

Isso criará um novo diretório chamado `nome_do_ambiente` que conterá todos os arquivos necessários para o ambiente virtual.

### Ativando o Ambiente Virtual

Depois de criar o ambiente virtual, você precisa ativá-lo. No Windows, você pode fazer isso executando o seguinte comando no prompt de comando:

```bash
nome_do_ambiente\Scripts\activate
```

No Linux/macOS, você pode usar o seguinte comando no terminal:

```bash
source nome_do_ambiente/bin/activate
```

Quando o ambiente virtual estiver ativado, o prompt de comando será alterado para indicar o nome do ambiente entre parênteses, indicando que o ambiente virtual está ativo.

### Desativando o Ambiente Virtual

Para desativar o ambiente virtual e retornar ao ambiente Python global, você pode simplesmente executar o seguinte comando:

```bash
deactivate
```

Isso irá restaurar o ambiente Python global e você retornará ao prompt de comando normal.

## Exemplo de Uso do Pacote `requests` com a API do GitHub

Vamos usar o pacote externo `requests` para fazer uma solicitação GET para a API do GitHub. Certifique-se de instalá-lo primeiro usando o seguinte comando:

```bash
pip install requests
```

Aqui está um exemplo simples de como usar o pacote `requests` para fazer uma solicitação GET para a API do GitHub e exibir informações sobre um repositório público:

```python
import requests

# Fazendo uma solicitação GET para a API do GitHub
response = requests.get("https://api.github.com/repos/LucasHenriqueAbreu/logica-e-fundamentos-de-programacao")

# Verificando se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    data = response.json()
    print("Informações sobre o repositório:")
    print("Nome:", data["name"])
    print("Descrição:", data["description"])
    print("URL:", data["html_url"])
    print("Número de estrelas:", data["stargazers_count"])
    print("Número de forks:", data["forks_count"])
else:
    print("Ocorreu um erro ao fazer a solicitação:", response.status_code)
```

Este exemplo faz uma solicitação GET para a API do GitHub para obter informações sobre o repositório "Hello-World" do usuário "octocat" e exibe o nome, descrição e URL do repositório.

## Resumo

- **Pacotes Externos**: São bibliotecas ou módulos desenvolvidos por terceiros que oferecem funcionalidades adicionais.
- **Ambientes Virtuais**: São ambientes Python isolados que permitem gerenciar dependências e pacotes para projetos específicos.

## Recursos Adicionais

- [Documentação Oficial do Python sobre Pacotes](https://packaging.python.org/tutorials/installing-packages/)
- [Documentação Oficial do Python sobre Ambientes Virtuais](https://docs.python.org/3/library/venv.html)

Explore esses recursos para aprofundar seu entendimento sobre pacotes externos e ambientes virtuais em Python.
