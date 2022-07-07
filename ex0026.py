#este programa identifica as posições das letras de uma frase qualquer

nome = str(input('Escreva o seu nome: ')).upper().strip()
print('A letra A aparcece {} vez na frase'.format(nome.count('A')))
print('A primeira vez que ocorre a letra A é na posição {}'.format(nome.find('A')+1))
print('A última vez que ocorre a letra A na frase é na posição {}'.format(nome.rfind('A')+1))


