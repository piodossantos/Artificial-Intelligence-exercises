""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import sin,sqrt
from .problem import OptimizationProblem

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
    #divmod(x0)
    if len(elemsList)!=len(list(set(elemsList))):
        return -65
    c=1
    for x in elem:
        if c>0:
            for y in elem:
                if x!=y:
                    if ((x-y)%7==0)or((x-y)%9==0):
                        print("entro "+str(x)+" "+str(y))
                        c=-1
                        break
    return (c)*sum([board[x] for x in elem])

BUKING_N6=OptimizationProblem(domains= ((-15,-5),(-3,3)), objective=__bukin_N6__)
SCHAFFER_N2 = OptimizationProblem(domains= ((-100,+100),)*2, objective=__schaffer_N2__)
ALFILES = OptimizationProblem(domains= ((0,63),)*8,objective=alfiles)
