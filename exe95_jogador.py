jogador = dict()
partidas = list()
jogador['nome'] = str(input('Qual o nome do jogador: '))
total = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou: '))

for c in range(total):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}ª foi feito: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(f' {jogador["nome"].upper()} jogou {len(jogador["gols"])} partidas')
print('-=' * 30)
for k, v in enumerate(jogador["gols"]):
    print(f'    ==> Na  {k + 1}ª partida, fez {v} gols')

print('-=' * 30)
print(f'O jogador {jogador["nome"].title()} fez {jogador["total"]}  gols')