preco = float(input('Digite o Preço do Produto?R$ '))
novo = preco - (preco * 5 /100)
print('O Produto que custava R${:.2f} sai com 5% de desconto vai custar R${:.2f}'.format(preco, novo))
