peso = float(input('Qual e seu peso? (Kg) '))
altura = float(input('Qual e sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('PARABENS, voce esta na faixa de peso normal!')
elif 25 <= imc < 30:
    print('Voce esta acima do peso normal')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Voce esta em OBESIDADE MORBIDA, cuidado!')
