print('\033[1;31;47mMedidor de temperatura\033[m')
C = float(input('Informe a Temperatura em °C ' ))
F = ((9*C) / 5) + 32
print('A Temperatuda de {}°C corresponde a {} °F:'.format(C, F))
print('\033[1;31mFIM\033[m')

