import random
import math
import copy
def DeckCards():
	cards=[]
	#"♠♥♦♣"
	#["Diamond","Club","Heart","Spade"]
	for i in "♠♥♦♣":
		k = 0
		for j in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
			cards+= [(j+" "+i+" ",k)]
			k+=1
	cards2=[]
	for i in range(52):
		cards2+=[cards.pop(random.randint(0,len(cards)-1))]
	return cards2

# lista montones [1,3,4,5]
def RandomDeckCards(overlapping_list):
	deck = DeckCards()
	result = []
	for i in overlapping_list:
		result+=[[deck.pop(random.randint(0,len(deck)-1)) for _ in range(i)]]
	result+=[[deck.pop(random.randint(0,len(deck)-1))]]
	result+=[deck]
	return result

# successores
def successor(deck):
	number_decks= len(deck) -2
	foundation= deck[-2][-1]
	result=[]
	for i in range(number_decks):
		if deck[i] != [] :
			if deck[i][-1][1]==((foundation[1] + 1)%13):
				result+=[i]
			elif deck[i][-1][1]==((foundation[1] - 1)%13):
				result+=[i]
	if len(deck[-1]) != 0:
		result+=[-1]
	return result

def search1(problem):
	for _ in range(2500):
		deck = RandomDeckCards(problem)
		if goalTest1(problem,copy.deepcopy(deck)):
			return deck
	raise Exception("Search 1: Fail")

def goalTest1(problem,solution):
	if len(problem)!=(len(solution)-2):
		print("entro aca")
		return False
	p=0
	for i in problem:
		if len(solution[p])!=i:
			print("entro a monton distinto.")
			return False
		p+=1
	try:
		a=search2(solution)
	except Exception as e:
		a=False
	finally:
		return a

def search2(problem):
	result = search2_recursive_heuristic(problem,[])
	if result[0]:
		return result[1]
	raise Exception("Search 2: Fail")

def search2_recursive(game,sequence):
	##El test objetivo podria plantearse como problema, y secuencia, pero no es eficiente cuando se recorren millones de nodos
	##una simplificacion es manejar el estado actual del juego, recalcularlo cada vez que se va a evaluar no es eficiente.
	if goalTest2(game,sequence):
		return (True,sequence)
	successores = successor(game)
	for s in successores:
		game[-2]+=[game[s].pop()]
		(result,new_path)= search2_recursive(game,sequence+[s])
		if result:
			return (True,new_path)
		game[s]+=[game[-2].pop()]
	return (False,sequence)

def goalTest2(problem,solution):
	return sum(problem[:-2])== 0
	#return len(problem[-2])==52

def search2_recursive_heuristic(game,sequence):
	if goalTest2(game,sequence):
		return (True,sequence)
	s = sucesor_heuristic(game)
	print(s)
	if s == None :
		print("Imprime none")
		return (False,sequence)
	game[-2]+=[game[s].pop()]
	print("Largo del mazo"+len(deck[-1]))
	return search2_recursive_heuristic(game,sequence+[s])


def sucesor_heuristic(deck):
	number_decks= len(deck) -2
	foundation= deck[-2][-1]
	result=[]
	for i in range(number_decks):
		if deck[i] != [] :
			if deck[i][-1][1]==((foundation[1] + 1)%13):
				result+=[i]
			elif deck[i][-1][1]==((foundation[1] - 1)%13):
				result+=[i]
	print(result)
	if result != []:
		print("Entro aca")
		aux = [len(deck[i]) for i in result]
		maximum = max(aux)
		print("Entro acaaa")
		print(result[result.index(maximum)])
		return result[result.index(maximum)]
	if len(deck[-1]) != 0:
		print("Devuelve Carta del mazo")
		return (-1)
	return None

def printGame(game):
	for i in range(len(game)-2):
		print("Mazo "+str(i)+":"+str([j[0] for j in game[i]]))
	print("Fundacion: "+str(game[-2][0][0]))
	print("Mazo sin descubrir: "+str([j[0] for j in game[-1]]))


def testRandomDeck():
	print("\nEjemplo de movientos disponibles en mazo aleatorio\n")
	result = RandomDeckCards([7,7,7,7,7,7])
	printGame(result)
	print("Sucsores: "+ str(successor(result)))

def testSearch1():
	print("\nBusqueda de solucion a un juego\n")
	overlapping_list = [1]
	juego = RandomDeckCards(overlapping_list)
	#printGame(juego)
	try:
		juego = search2(juego)
		print("Camino: " + str(juego))
	except Exception as e:
		print("Este juego no tiene Solucion")


def testSearch2():
	print("\nEjemplo de Busqueda de juego que pueda resolverse\n")
	a = search1([2,1])
	printGame(a)

testSearch1()
#testSearch2()
#testRandomDeck()
