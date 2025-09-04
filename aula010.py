n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n2 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n2)/3
print('A sua media foi {:.1f}'.format(m))
print('Parabens' if m >=6 else 'Estude MAIS!')