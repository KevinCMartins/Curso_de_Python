salario = (float(input('Qual e o salario do Funcionario? R$')))
novo = salario +(salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, R${:.2f}'.format(salario, novo))