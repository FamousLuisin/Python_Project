import os

# criar tabuleiro
def create_a_board():
    tabuleiro= []
    for i in range(3):
        tabuleiro.append([])
        for _ in range(3):
            tabuleiro[i].append(None)

    return tabuleiro


# Ver tabuleiro (tabuleiro)
def see_board(board):
    for line in board:
        for valor in line:
            if valor == None:
                print('|-', end='|')
            elif valor == 0:
                print('|O', end='|')
            else:
                print('|x', end='|')
        print()



# Trocar / mudar de jogador
def change_player(player):
    # Alterar jogador
    if player == 0:
        return 1
    return 0

# Essa função serve para fazer e validar uma jogada
def move(player, board):
    see_board(board)
    while True:
        line = int(input('Linha da jogada: '))

        column = int(input('coluna da jogada: '))

        try:
            if board[line][column] is None:
                board[line][column] = player
                return board
            print('Linha ou Coluna inválido')

        except IndexError:
            print('Linha ou Coluna inválido')


# Essa função analisa o tabuleiro para ver se alguem ganhou
def analyze_board(board):
    # Analisar linha
    for line in board:
        if None in line:
            continue
        if sum(line) == 0 or sum(line) == 3:
            return True

    # Analisar colunas
    for column in range(3):
        soma = 0
        for line in range(3):
            try:
                soma = soma + board[line][column]
            except TypeError:
                soma = -1
                break
        if soma == 0 or soma == 3:
            return True

    # Analisar Diagonal
    try:
        soma = board[0][0] + board[1][1] + board[2][2]
        if soma == 0 or soma == 3:
            return True

    except TypeError:
        ...

    try:
        soma = board[0][2] + board[1][1] + board[2][0]
        if soma == 0 or soma == 3:
            return True
    except TypeError:
        ...

    return False


# Analisar se houve empate
def analyze_draw(board):
    if not None in board[0] and not None in board[1] and not None in board[2]:
        return True
    return False


# Função main / principal
def main():
    print('Jogo da velha\n')

    # Criar o tabuleiro
    board = create_a_board()
    player = 0

    winner = False

    while True:
        os.system('cls')
        print(f'Jogador {player}:')
        board = move(player, board)
        
        if analyze_board(board):
            winner = True
            break

        if analyze_draw(board):
            break

        player = change_player(player)

    see_board(board)
    if winner:
        print(f'O ganhador é o jogador {player}')
    else:
        print('Sem ganhador')

main()