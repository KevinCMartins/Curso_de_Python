preco = float(input('Qual e o preco do produto? R$'))
novo = preco - (preco *5 / 100)
print('O produto que custava {:.2f}, na promocao com desconto de 5% vai custar R${:.2f}.'.format(preco, novo))
