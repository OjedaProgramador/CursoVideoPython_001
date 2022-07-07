vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input('Escreva uma frase: '))

new_vogal = {} #------> iniciou um dicionario { }
new_vogal['a'] = 0
new_vogal['e'] = 0
new_vogal['i'] = 0
new_vogal['o'] = 0
new_vogal['u'] = 0
for c in palavra:
    if c in vogais:
        new_vogal[c] += 1
for k, v in sorted(new_vogal.items()):
    print(f'A letra {k} apareceu {v} vezes nesse nome')
