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
	if len(deck[-1]) != 0:
		result+=[-1]
	for i in range(number_decks):
		if deck[i] != [] :
			if deck[i][-1][1]==((foundation[1] + 1)%13):
				result+=[i]
			elif deck[i][-1][1]==((foundation[1] - 1)%13):
				result+=[i]
	return result

def search1(problem):
	for _ in range(25):
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
	result = search2_recursive(problem,[])
	if result[0]:
		return result[1]
	raise Exception("Search 2: Fail")

def search2_recursive(game, sequence):
	if goalTest2(game,sequence):
		return (True,sequence)
	successores = successor(game)
	for s in successores:
		#print(len(game[-2]))
		game[-2]+=[game[s].pop()]
		(result,new_path)= search2_recursive(game,sequence+[s])
		if result:
			return (True,new_path)
		game[s]+=[game[-2].pop()]
	return (False,sequence)

def goalTest2(problem,solution):
	return len(problem[-2])==52

def test():
	result = RandomDeckCards([7,7,7,7,7])
	print("tope mazos en mesa")
	for i in range( len(result)-2):
		print(result[i][-1][0])
	print("Fundacion")
	print(result[-2][-1][0])
	print("Tope Mazo ")
	print(result[-1][-1][0])
	print("Combinaciones posibles")
	print(successor(result))
def test1():
	juego = RandomDeckCards([48,1])
	for i in range(4):
		print("Mazo "+str(i)+":"+str([j[0] for j in juego[i]]))
	print("Foundation: "+str(juego[-2]))
	print("Mazo: "+str([j[0] for j in juego[-1]]))
	juego = search2(juego)
	print(len(juego),juego)


def test2():
	a = search1([49,1])
	print(a)
test2()
