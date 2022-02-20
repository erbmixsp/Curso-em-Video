print('\033[31;43mCalculo Para Pintar uma Parede\033[m')
print('='*60)

larg = float(input('Digite a Largura:'))
alt = float(input('Digite a Largura: '))
area = larg*alt
print('Sua Parede tem a Dimensão de: {}m² x {}m² e Sua area é de {}m²'.format(
    alt, larg, area))
tinta = area / 2
print('Para pintar essa parede, vc precisará de: {}L de tinta'.format(tinta))
print('='*60)
print('\033[31;43mFIM\033[m')


