pessoa = {}
pessoa['name'] = input('Informe seu nome: ')
pessoa['email'] = input('Informe o seu email: ')
pessoa['endereco'] = input('Informe o seu endereço: ')

for key in pessoa.keys():
    print(key, pessoa[key])