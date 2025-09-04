real = float(input('Quanto dinheiro voce tem na carteira? R$'))
euro = real / 6.1
libra = real / 7.3
dolar = real / 5.8
print('Com R${:.2f} voce pode comprar EU£{:.2f}'.format(real, euro))
print('Com R${:.2f} voce pode comprar GBP£{:.2f}'.format(real, libra))
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))