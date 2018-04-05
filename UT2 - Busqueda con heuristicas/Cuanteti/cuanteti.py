import random

__author__ = "Equipo Pro"


def playGame():
    game = [" " for _ in range(16)]
    player = True
    while playing(game):
        print(board(game))
        position = int(input("Juega " + ("X" if player else "O") + ".\nIngrese Posicion"))
        if position < 0 or position > 15:
            print("Debe seleccionar Posicion Valida")
        elif game[position] != " ":
            print("La posicion esta ocupada")
        else:
            game[position] = "X" if player else "O"
            player = not player
    print(board)
    print("El juego ha terminado.")
    w = winner(game)
    if w == "E":
        print("Empate")
    else:
        print("El Ganador es: " + w)


def board(game):
    return f"{'|'.join(game[:4])}\n{'|'.join(game[4:8])}\n{'|'.join(game[8:12])}\n{'|'.join(game[12:])}"


def winner(game):
    combos = winning_combos(game)
    score = 0
    sgn = 1
    for p in "XO":
        for combo in combos:
            if len(combo) > 3:
                if (p + p + p + p) in combo:
                    score += (sgn * 2)
                    print(sgn * 2)
                elif (p + p + p) in combo:
                    score += sgn
                    print(sgn)
            else:
                if (p + p + p) in combo:
                    score += sgn
                    print(sgn)
        sgn = -1
    print("score = "+str(score))
    return "X" if score > 0 else ("E" if score == 0 else "O")


def winning_combos(game):
    separator = ""
    result = [(separator.join([game[j] for j in range(0, 16) if j % 4 == i])) for i in range(4)]
    result += [separator.join(game[i: i + 4]) for i in range(0, 16, 4)]
    result += [separator.join([game[8], game[5], game[2]])]
    result += [separator.join([game[12], game[9], game[6], game[3]])]
    result += [separator.join([game[13], game[10], game[7]])]
    result += [separator.join([game[4], game[9], game[14]])]
    result += [separator.join([game[0], game[5], game[10], game[15]])]
    result += [separator.join([game[1], game[6], game[11]])]
    return result


def playing(game):
    return " " in game


def test1():
    testGame = ["X" for _ in range(8)] + ["O" for _ in range(8)]
    random.shuffle(testGame)
    print(board(testGame))
    print(winner(testGame))


# playGame()
test1()
