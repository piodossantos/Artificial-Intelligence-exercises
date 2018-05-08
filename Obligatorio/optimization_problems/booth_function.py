from math import *
from problem import OptimizationProblem
import random

acc = [0]
def __booth__(elem):
    acc[0]+=1
    (x1,x2)=elem
    return (x1+2*(x2)-7)**2+(2*(x1)+x2-5)**2

PROBLEM = OptimizationProblem(domains= ((-10,10),)*2, objective=__booth__)
