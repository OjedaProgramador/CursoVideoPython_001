temp = list()
principal = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break


print(f'Ao todo você cadastrou {len(principal)} pessoas')
print(f'o maior peso foi {maior}')

for p in principal:
    if p[1] == maior:
        print(f'A pessoa mais pesada cadastrada é[{p[0]}] com {maior} Kg')
print('--#--' * 10)

for p in principal:
    if p[1] == menor:
        print(f'A pessoa mais leve cadastrada é [{p[0]}] com {menor}Kg')


print('Fim do cadastro')