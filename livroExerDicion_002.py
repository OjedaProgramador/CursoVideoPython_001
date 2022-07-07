'''frase = 'gabriel viviane livia'
new_frase = list(frase)
for nome in new_frase[:7]:
    print('\t' * 2, nome)
for nome in new_frase[8:15]:
    print('\t' * 3, nome)
for nome in new_frase[-5:]:
    print('\t' * 4, nome)'''

#-------------------------------------------------
'''pessoa = {'nome': 'Ojeda',
          'idade': 46,
          'privilegio': 'Ancião',
          'marido': 'Viviane',
          'pai': 'Lívia'}

while True:
    resp = str(input('Qaul a senha: '))
    if resp in 'ojeda':
        for k, v in pessoa.items():
            print(k)
        print('fim do programa')
        break'''

dadosGeral = [[], []]
juntos = ' '
cont = 0
while True:
    dadosGeral[0] = str(input('Esvreva um nome: '))
    dadosGeral[1] = int(input('Qual a idade: '))
    cont += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            for c in range(len(dadosGeral)):
                print(f'{dadosGeral[0]} tem {dadosGeral[1]} anos de idade')
            break

