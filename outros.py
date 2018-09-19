import random as random
pecas = []
mesa = []
lados = [1, 2]


def colorirpontas():
    print("\033[32m" + str(mesa[0]) + "\033[0;0m", "".join(str(p) for p in mesa[1: -1]), "\033[32m" +
          str(mesa[-1]) + "\033[0;0m")


nome1 = input("Insira o nome do jogador 1: ")
nome2 = input("Insira o nome do jogador 2: ")

# criando as pecas do jogo de dominó

for i in range(7):
    for x in range(i, 7):
        pecas.append([i, x])


# distribuindo 7 peças para cada jogador

player1 = []
player2 = []

while len(player1) < 7:
    qtd_pecas = len(pecas)
    i = random.randrange(qtd_pecas)
    player1.append(pecas[i])
    pecas.remove(pecas[i])
    qtd_pecas = len(pecas)
    i = random.randrange(qtd_pecas)
    player2.append(pecas[i])
    pecas.remove(pecas[i])


# começando o jogo


for i in range(6, -1, -1):
    if [i, i] in player1:
        ii = player1.index([i, i])
        mesa.append(player1.pop(ii))
        break
    elif [i, i] in player2:
        ii = player2.index([i, i])
        mesa.append(player2.pop(ii))
        break

print("\n", mesa, "\n")

# Definindo função para jogadas


def turns(player, nome):
    continua = 0
    while continua == 0:
        print(nome, ", auas peças:")
        for x in range(len(player)):
            print("%i = " % x, player[x])
        y = int(input("%s, escolha a peça a ser jogada (99 para comprar):" % nome))
        while y not in [99]+list(range(len(player))):
            print("Resposta inválida!")
            y = int(input("%s, escolha a peça a ser jogada (99 para comprar):" % nome))
        else:
            if y == 99:
                qtd_pecas = len(pecas)
                if qtd_pecas == 0:
                    print("Não há mais peças para comprar...")
                    continua = 1
                else:
                    i = random.randrange(qtd_pecas)
                    player.append(pecas.pop(i))
            elif player[y][1] == mesa[0][0] and player[y][1] == mesa[-1][1]:
                lado = int(input("Em qual lado você deseja colocar a peça?(1 para esquerda, 2 para direita): "))
                if lado == 1:
                    mesa.insert(0, player.pop(y))
                    colorirpontas()
                    continua = 1
                elif lado == 2:
                    player[y].reverse()
                    mesa.append(player.pop(y))
                    colorirpontas()
                    continua = 1
            elif player[y][0] == mesa[0][0] and player[y][0] == mesa[-1][1]:
                lado = int(input("Em qual lado você deseja colocar a peça?(1 para esquerda, 2 para direita): "))
                if lado == 2:
                    mesa.append(player.pop(y))
                    colorirpontas()
                    continua = 1
                elif lado == 1:
                    player[y].reverse()
                    mesa.insert(0, player.pop(y))
                    colorirpontas()
                    continua = 1
            elif player[y][0] == mesa[0][0] and player[y][1] == mesa[-1][1]:
                lado = int(input("Em qual lado você deseja colocar a peça?(1 para esquerda, 2 para direita): "))
                if lado == 2:
                    player[y].reverse()
                    mesa.append(player.pop(y))
                    colorirpontas()
                    continua = 1
                elif lado == 1:
                    player[y].reverse()
                    mesa.insert(0, player.pop(y))
                    colorirpontas()
                    continua = 1
            elif player[y][1] == mesa[0][0] and player[y][0] == mesa[-1][1]:
                lado = int(input("Em qual lado você deseja colocar a peça?(1 para esquerda, 2 para direita): "))
                if lado == 2:
                    mesa.append(player.pop(y))
                    colorirpontas()
                    continua = 1
                elif lado == 1:
                    mesa.insert(0, player.pop(y))
                    colorirpontas()
                    continua = 1
            elif player[y][1] == mesa[0][0]:
                mesa.insert(0, player.pop(y))
                colorirpontas()
                continua = 1
            elif player[y][0] == mesa[-1][1]:
                mesa.append(player.pop(y))
                colorirpontas()
                continua = 1
            elif player[y][0] == mesa[0][0]:
                player[y].reverse()
                mesa.insert(0, player.pop(y))
                colorirpontas()
                continua = 1
            elif player[y][1] == mesa[-1][1]:
                player[y].reverse()
                mesa.append(player.pop(y))
                colorirpontas()
                continua = 1
            else:
                print("Resposta inválida!!!")
                colorirpontas()

# Dinâmica do jogo e estado de finalização


if len(player1) < len(player2):
    while len(player1) and len(player2) != 0:
        turns(player2, nome2)
        turns(player1, nome1)

    else:
        if len(player1) == 0:
            print(nome1, " Venceu!!")
        elif len(player2) == 0:
            print(nome2, " Venceu!!")

elif len(player1) >= len(player2):
    while len(player1) and len(player2) != 0:
        turns(player1, nome1)
        turns(player2, nome2)

    else:
        if len(player1) == 0:
            print(nome1, " Venceu!!")
        elif len(player2) == 0:
            print(nome2, " Venceu!!")
