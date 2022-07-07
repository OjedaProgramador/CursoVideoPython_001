from random import randint
from time import sleep
pc = randint(0,2) # faz o computador pensar em coisas aleadorias
print('----><----'*10)
print('Tente adivinhar o número que será escolhido entre 0 até 9')
print('<------->'*13)
jogador = int(input('Qual foi o número que eu pensei: ')) # jogor tenta adivinhar o número
print('PROCESSANDO . . . ')
sleep(2)
print('PROCESSANDO . . . ')
sleep(2)
if jogador == pc:
    print('Parabéns, você é muito esperteleco!!!')
else:
    print('Tente novamente -----> VOCÊ ERROU')

print('O número escolhido foi {}'. format(pc))
