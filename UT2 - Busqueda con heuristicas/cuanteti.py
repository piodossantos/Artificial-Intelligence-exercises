import random
import math
__author__ = "Equipo Pro"




def playGame():
    game = [" " for _ in range(16)]
    player = True
    while playing(game):
        print(board(game))
        if player:
            position = int(input("\nJuega " + ("X" if player else "O") + ".\nIngrese Posicion: "))
        else:
            print("\nJuega " + ("X" if player else "O"))
            position = int(heuristic(game))
            #print(str(position))
        if position < 0 or position > 15:
            print("Debe seleccionar Posicion Valida")
        elif game[position] != " ":
            print("La posicion esta ocupada")
        else:
            game[position] = "X" if player else "O"
            player = not player
    print("El juego ha terminado.")
    w = winner(game)
    if w == "E":
        print("Empate")
    else:
        print("El Ganador es: " + w)



def board(game):
    return "{}\n{}\n{}\n{}\n".format('|'.join(game[:4]),'|'.join(game[4:8]),'|'.join(game[8:12]),'|'.join(game[12:]))

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

def heuristic(game):
    diagonals = [
    [8,5,2],
    [12,9,6,3],
    [13,10,7],
    [4,9,14],
    [0,5,10,15],
    [1,6,11]
    ]
    positions = [(i,0) for i in range(0,16) if game[i]==" "]
    for p in range(len(positions)):
        combos = []
        i = math.floor(positions[p][0]/16)
        j = positions[p][0]%16
        combos+=[''.join(game[i:i+4])]
        combos+=[''.join([game[k] for k in range(16) if k%4 == j])]
        for f in diagonals:
            if positions[p][0] in f:
                combos+=[''.join([game[w] for w in f])]
        for c in combos:
            if len(c)>3:
                points = abs((c.count("X")-c.count("0"))**3)+c.count(' ')**(1/2)
            else:
                points = (c.count("X")-c.count("0"))**2+c.count(' ')**(1/2)
            positions[p]=(positions[p][0],points+positions[p][1])
    result=(-1,-1)
    best=[]
    print(positions)
    for p in positions:
        result = p if p[1] > result [1] else result
    for p in positions:
        if p[1]==result[1]:
            best+=[result]
    print(best)
    return random.choice(best)[0]
def test1():
    testGame = ["X" for _ in range(8)] + ["O" for _ in range(8)]
    random.shuffle(testGame)
    #print(board(testGame))
    #print(winner(testGame))

def test2():
    testGame =[random.choice(["X","O"," "]) for _ in range(16) ]
    #print(board(testGame))
    #print(heuristic(testGame))
playGame()
#test1()
#test2()
