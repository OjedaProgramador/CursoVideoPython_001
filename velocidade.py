
carro =float(input('O carro passou em qual velocidade?: '))

multa = (carro - 80) * 7
multa02 = (carro  - 120) * 14
if carro <= 80:
    print('Você está dirigindo com segurança !!!')
elif 81 <= carro <= 120:

    print('voce foi multado em R$:{:.2f} '.format(multa))
else:

        print('A sua multa é maior pq voce dirigiu a cima de 120km/h,\n sua multa é R$:{}'.format(multa + multa02))


print(multa)
print(multa02)

