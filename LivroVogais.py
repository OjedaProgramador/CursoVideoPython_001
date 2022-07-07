'''vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input('Escreva uma Palavra: '))
dicVogal = {}
for c in palavra:
    if c in vogais:
        dicVogal.setdefault(c, 0)
        dicVogal[c] += 1
for k, v in sorted(dicVogal.items()):
    print('A letra', k, 'apareceu', v,  'vezes')
-----------------------------------------------'''


'''a = set('aeiou')
b = 'conceição'
c = a.union(set(b))
print(sorted(c))
--------------------------------------------'''

'''a = set('aeiou')
b = 'conceição'
c = a.difference(set(b))
print(sorted(c))
------------------------------------------------'''

'''a = set('aeiou')
b = 'ana gonçalves'
c = a.intersection(set(b))
print(sorted(c))
-------------------------------------------------'''

vogais = set('aeiou') # --> é um dicionario
palavra = str(input('escreva uma palavra:'))
aqui = vogais.intersection(set(palavra))

for vogais in aqui:
    print(vogais)