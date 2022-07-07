frase = str(input('escreva algo: ')).strip().upper()

frase01 = len(frase)
if frase01 == 7:
    print('Você é o escolhido {}, porque seu nome tem {} letras'.format(frase, frase01))
else:
    print('Seu nome não tem a quantidade de letras corretas')
    print('Tente novamente ')
