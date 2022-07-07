def media (h, d):
    r = h / d
    print(f'A média de horas é de {r:.2f}')



h = float(input('Quantas horas você fez: '))
d = int(input('Quantos dias você trabalhou: '))
media(h, d)
