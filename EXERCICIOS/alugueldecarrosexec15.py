dias = int(input('Quantos dias Alugados?' ))
km = float(input('Quantos Kilometros Rodados? '))
pago = (dias * 60 ) + (km * 0.15)
print('O Total a pagar é de R${:.2f}'.format(pago))
