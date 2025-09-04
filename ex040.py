nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.2f} e {:.2f}, a media e {:.2f}'.format(nota1, nota2, media))
if 6 > media >= 5:
    print('O aluno esta em RECUPERACAO!')
elif media < 5:
    print('O aluno esta REPROVADO!')
else:
    print('O aluno esta APROVADO')
