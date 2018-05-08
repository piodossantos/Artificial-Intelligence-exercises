from math import *
from problem import OptimizationProblem
import random

def __schaffer_N2__(elem):
    print(elem)
    (x,y) = elem
    return 0.5 + (sin(x*x - y*y) ** 2 - 0.5)/((1 + 0.001 * (x*x + y*y)) ** 2)
SCHAFFER_N2 = OptimizationProblem(domains= ((-100,+100),)*2, objective=__schaffer_N2__)
