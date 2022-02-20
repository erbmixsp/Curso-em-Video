# uso do strip para tirar espaços do inicio da frase
nome = str(input('Digite seu nome completo?: ')).strip()
# uso do in e do lower para converter tudo em minusculos
print('Seu Nome Possui Silva. {}'.format('silva' in nome.lower()))
