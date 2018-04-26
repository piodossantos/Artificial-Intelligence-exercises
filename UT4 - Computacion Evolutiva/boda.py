import random
import numpy
import math
from deap import base, creator, tools, algorithms

#TARGET = "Hello world!"

#IND_SIZE = len(TARGET)
#INT_MIN, INT_MAX = 32, 126
IND_SIZE = 70
INT_MIN, INT_MAX = 0,11
# type
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# initialization
toolbox = base.Toolbox()
toolbox.register("attribute", random.randint, INT_MIN, INT_MAX)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evaluate(elem):
    #afinidad = [[random.randint(-1,1) for _ in range(70)] for _ in range(70)]
    #print(elem)
    afinidad = mat(70)
    elem = list(elem)
    flag = False
    errores = 0
    for e in elem:
        if elem.count(e)>6:
            flag=True
            errores+=1
            #errores+=elem.count(e)-6
    if flag:
        return (-71-errores),
    number = list(enumerate(elem))
    number.sort(key=lambda x: x[1])
    mesas = [[x for (x,y) in number if y==i ] for i in range(12)]
    acc=0
    for mesa in mesas:
        for p in mesa:
            for j in mesa:
                if p<j:
                    acc+=afinidad[p][j]
    return acc,
def mat(a):
	m = [[3 for _ in range(a)]for _ in range(a)]
	total = int(a*(a-1)*0.5)
	elem = [0 for _ in range(math.ceil(total * 0.5))]+[1 for _ in range(math.ceil(total * 0.3))]+[-1 for _ in range(math.ceil(total * 0.2))]
	for i in range(a):
		m[i][i]=1
	for i in range(a):
		for j in range(a):
			if i<j:
				e = elem.pop(random.randint(0,len(elem)-1))
				m[i][j]=e
				m[j][i]=e
	return m
# # operators
# def evaluate(individual):
#     score = 0
#     for index, c in enumerate(individual):
#         if chr(c) == TARGET[index]:
#             score += 1
#     return score,  # tuple


toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=INT_MIN, up=INT_MAX, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)


def evolution(CXPB=0.5, MUTPB=0.2, NGEN=30, n=1000):
    # create population
    pop = toolbox.population(n)
    #CXPB, MUTPB, NGEN = 0.5, 0.3, 30

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, stats=stats, halloffame=hof,
                                   verbose=True)

    return hof.items[0]



def test1(CXPB=0.5, MUTPB=0.2, NGEN=30, n=1000):
    print("# Problema de la Boda #")
    best = evolution(CXPB, MUTPB, NGEN, n)
    flag = [True]*12==[(best.count(i)<=6) for i in range(12)]
    if flag:
        print("La mejor solucion es: "+ str(best))
    else:
        print("No encontro solucion, la mas aproximada fue: "+str(best)) 

#if __name__ == "__main__":
#    best = evolution()
#    print(best)
    # # print word
    # word = ""
    # for character in best:
    #     word += chr(character)
    # print(word)
