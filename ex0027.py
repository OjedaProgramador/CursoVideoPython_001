#esse programa consegue mostar a primeira palavra e também a última palavra


n = str(input('Digite seu nome completo: ')).strip().upper()
nome = n.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome)-1]))


