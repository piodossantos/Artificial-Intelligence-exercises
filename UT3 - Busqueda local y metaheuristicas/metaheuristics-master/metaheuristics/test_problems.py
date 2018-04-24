""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import *
from .problem import OptimizationProblem
import random
def hello_world(target_str="Hello world!"):
    target_chars = tuple(map(ord, target_str))
    return OptimizationProblem(
        domains = ((32, 126),) * len(target_str),
        objective = lambda chars: sum(abs(c - t) for (c, t) in zip(chars, target_chars))
    )

# References:
# + [Test functions for optimization @ Wikipedia](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
# + [Test functions and datasets @ Virtual Library of Simulation Experiments](https://www.sfu.ca/~ssurjano/optimization.html)

def __bukin_N6__(elem):
    (x,y) = elem
    op1 = sqrt(abs(y-(0.01*x*x)))
    op2 = 0.01*abs(x+10)
    return 100*op1 + op2
def __schaffer_N2__(elem):
    (x,y) = elem
    return 0.5 + (sin(x*x - y*y) ** 2 - 0.5)/((1 + 0.001 * (x*x + y*y)) ** 2)

def alfiles(elem):
    board = [
    1,2,3,2,6,8,7,2,
    8,6,2,5,1,3,1,4,
    7,1,5,4,2,5,6,8,
    2,8,4,7,5,1,4,3,
    4,3,7,2,3,8,5,1,
    6,5,6,3,4,7,8,3,
    3,7,1,8,6,2,4,6,
    8,4,5,6,7,5,1,7
    ]
    elemsList = list(elem)
    if len(elemsList)!=len(list(set(elemsList))):
        return -65
    c=1
    elems=[divmod(x,8) for x in elem]
    diagons=[]
    for (a,b) in elems:
        if c>0:
            diagons =  [(a+i,b+i) for i in range(1,8) if (a+i)<=7 and (b+i)<=7]
            diagons += [(a-i,b-i) for i in range(1,8) if (a-i)>=0 and (b-i)>=0]
            diagons += [(a-i,b+i) for i in range(1,8) if (a-i)>=0 and (b+i)<=7]
            diagons += [(a+i,b-i) for i in range(1,8) if (a+i)<=7 and (b-i)>=0]
        for d in diagons:
            if d in elems:
                c=-1
                break
        diagons=[]
    return (c)*sum([board[x] for x in elem])
def boda(elem):
    #afinidad = [[random.randint(-1,1) for _ in range(70)] for _ in range(70)]
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
        return -71-errores
    number = list(enumerate(elem))
    number.sort(key=lambda x: x[1])
    mesas = [[x for (x,y) in number if y==i ] for i in range(12)]
    acc=0
    for mesa in mesas:
        for p in mesa:
            for j in mesa:
                if p!=j:
                    acc+=afinidad[p][j]
    return max(acc,-71)
def mat(a):
	m = [[3 for _ in range(a)]for _ in range(a)]
	total = int(a*(a-1)*0.5)
	elem = [0 for _ in range(ceil(total * 0.5))]+[1 for _ in range(ceil(total * 0.3))]+[-1 for _ in range(ceil(total * 0.2))]
	for i in range(a):
		m[i][i]=1
	for i in range(a):
		for j in range(a):
			if i<j:
				e = elem.pop(random.randint(0,len(elem)-1))
				m[i][j]=e
				m[j][i]=e
	return m
BUKING_N6=OptimizationProblem(domains= ((-15,-5),(-3,3)), objective=__bukin_N6__)
SCHAFFER_N2 = OptimizationProblem(domains= ((-100,+100),)*2, objective=__schaffer_N2__)
ALFILES = OptimizationProblem(domains= ((0,63),)*8,target=inf,objective=alfiles)
BODA = OptimizationProblem(domains= ((0,11),)*70,target=inf,objective=boda)
