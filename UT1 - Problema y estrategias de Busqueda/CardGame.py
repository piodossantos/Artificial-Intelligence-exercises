import random
import math
def DeckCards():
	cards=[]
	#"♠♥♦♣"
	#["Diamond","Club","Heart","Spade"]
	for i in "♠♥♦♣":
		k = 0
		for j in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
			cards+= [(j+" "+i,k)]
			k+=1
	return cards

# lista montones [1,3,4,5]
def RandomDeckCards(overlapping_list):
	deck = DeckCards()
	result = []
	for i in overlapping_list:
		result+=[[deck.pop(random.randint(0,len(deck)-1)) for _ in range(i)]]
	result+=[[deck.pop(random.randint(0,len(deck)-1))]]
	result+=[deck]
	return result

# Sucesores
def sucesor(deck):
	cantidad_mazos= len(deck) -2
	tope_fundacion= deck[-2][-1]
	resultado=[]
	if len(deck[-1]) != 0:
		resultado+=[-1]
	for i in range(cantidad_mazos):
		if deck[i] != [] :
			if deck[i][-1][1]==((tope_fundacion[1] + 1)%13):
				resultado+=[i]
			elif deck[i][-1][1]==((tope_fundacion[1] - 1)%13):
				resultado+=[i]
	return resultado

def play(game, camino):
	if len(game[-2])==52:
		return (True,camino)
	sucesores = sucesor(game)
	for s in sucesores:
		#print(len(game[-2]))
		game[-2]+=[game[s].pop()]
		(resultado,new_path)= play(game,camino+[s])
		if resultado:
			return (True,new_path)
		game[s]+=[game[-2].pop()]
	return (False,camino)

def test():
	resultado = RandomDeckCards([7,7,7,7,7])
	print("tope mazos en mesa")
	for i in range( len(resultado)-2):
		print(resultado[i][-1][0])
	print("Fundacion")
	print(resultado[-2][-1][0])
	print("Tope Mazo ")
	print(resultado[-1][-1][0])
	print("Combinaciones posibles")
	print(sucesor(resultado))
def test1():
	juego = RandomDeckCards([5,4,4,5,1,1,2])
	print(juego)
	juego = play(juego,[])
	print(juego[0],len(juego[1]),juego[1])
test1()
