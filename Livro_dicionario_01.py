
def teste ():
    from pprint import pprint

    pessoas = {}
    pessoas['Ojeda'] = {'Nome': 'Gabriel Ojeda',
                        'Privilegio': 'Ancião',
                        'Batismo': '07011987',
                        'Telefone': 982027378}
    pessoas['Viviane'] = {'Nome': 'viviane Ojeda',
                        'Privilegio': 'Pioneira Regular',
                        'Batismo': '11082002',
                        'Telefone': 992213696}
    pessoas['Livia'] = {'Nome': 'Lívia Ojeda',
                        'Privilegio': 'Estudante Mirim',
                        'Batismo': 'não batizada',
                        'Telefone': 992867269}

    print(pprint(pessoas))



'''vogais = set('aeiou')
palavra = str(input('Escreva uma frase: '))
escolhida = vogais.intersection(set(palavra))'''

vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input('Escreva uma frase: '))
dicionario = {}
for c in  palavra:
    if c in vogais:
        dicionario.setdefault(c, 0)
        dicionario[c] += 1
for k, v in sorted(dicionario.items()):
    print(k, v)




