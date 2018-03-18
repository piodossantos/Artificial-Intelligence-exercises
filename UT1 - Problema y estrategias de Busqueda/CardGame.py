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
def RandomDeckCards(lista_montenes):
	deck = DeckCards()
	result = []
	for i in lista_montenes:
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
		resultado+=[deck[-1][-1]]
	for i in range(cantidad_mazos):
	#	print((deck[i][-1][1] - tope_fundacion[1])%12)
		#tope_fundacion[1]
		#deck[i][-1][1]
		if deck[i][-1][1]==((tope_fundacion[1] + 1)%13):
			resultado+=[deck[i][-1]]
		elif deck[i][-1][1]==((tope_fundacion[1] - 1)%13):
			resultado+=[deck[i][-1]]
	return resultado


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
