import random
card_values={"A":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"10":9,"J":10,"Q":11,"K":12}
def DeckCards():
	cards={}
	for i in ["Diamond","Club","Heart","Spade"]:
		for j in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
			temp=cards.get(j,[])+[(i,j)]
			cards[j]=temp
	return cards
##nCards = [3,2,4,5]
def Game(nCards):
	deck = DeckCards()
	overlapping =[]
	play_history =[]
	foundation =[]
	for i in range(len(nCards)):
		overlapping+=[[]]
	while sum(nCards) > sum([len(el) for el in overlapping]):
		number = random.randint(0,12);
		card = deck[number].pop()
		flag = True
		while flag:
			randOverlapping = random.randint(0,len(nCards)-1)
			if(len(overlapping[randOverlapping])<nCards[randOverlapping]):
				flag=False
				overlapping[randOverlapping]+=[card]
				play_history+=[randOverlapping]
	return(play_history)
##print(Game([3,4,5]))

def Suc(deck,nMovs,card):
	movs=[deck[(card[2]+1)%13]]
	movs+=[deck[(card[2]-1)%13]]
	movs=[item for sublist in movs for item in sublist]
	if (movs==[] and nMovs>0):
		movs= [item for sublist in deck.values() for item in sublist]
	return movs

def test():
	deck=DeckCards()
	deck.pop()
	print("Test 1: {} ".format(Suc(deck,1,("A","Diamond",0))))

#print(test())

print(DeckCards())
