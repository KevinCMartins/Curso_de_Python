velocidade = float(input('Qual e a velocicade do carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido e 80Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagr uma multa de R${:.2f}!'.format(multa))
elif velocidade < 80:
    print('Tenha um bom dia! Diriga com seguranca!')