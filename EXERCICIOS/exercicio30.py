numero = int(input('Digite um Numero? '))
resultado = numero % 2
if resultado == 0:  # condição simples
    print('{} O numero {} é Par'.format(
        '\33[4;32;40m', numero, '33[m'))  # resposta em verde
else:
    print('{} O numero {} é Impar'.format(
        '\33[4;31;40m', numero, '33[m'))  # resposta em vermelho
