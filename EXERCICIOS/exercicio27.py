
n = str(input('Digite Seu Nome Completo? ')).strip()# elimina espaços
nome = n.split() # split fatia o nome completo criando uma lista

print(nome[0])
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu Sobrenome é: {}'.format(nome[len(nome)-1]))# a função len busca o ultimo nome e -1 pois ele conta 0
