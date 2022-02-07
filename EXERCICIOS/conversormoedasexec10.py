real = float(input('Qunto vc Tem em sua carteira? R$ '))
print('-'*40)
dolar = real / 5.33
euro = real / 6.10
yuan = real / 0.84
print('Com R${:.2f} vc pode comprar US${:.2f} dolares'.format(real, dolar))

print('Ou R${:.2f} vc pode comprar €{:.2f} euros'.format(real, euro))
print(
    'Ou ainda com R${:.2f} vc pode comprar  ¥ {:.2f} yuan'.format(real, yuan))
print('-'*40)
