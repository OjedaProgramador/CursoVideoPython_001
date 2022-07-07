salario = float(input('Qual o seu salário atual: '))
if salario <= 1250:
    print(' Seu novo salário agora é {:.2f}'.format(salario + (salario * 15/100)))
else:
    print('Seu salário será {:.2f}'.format(salario + (salario * 10 / 100)))
