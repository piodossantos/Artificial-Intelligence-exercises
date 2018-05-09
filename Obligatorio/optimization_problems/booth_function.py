from math import *
from problem import OptimizationProblem
import random


flag=[True]
acc = [0]
def __booth__(elem):
    elem=list(elem)
    acc[0]+=1
    (x1,x2)=elem
    v= (x1+2*(x2)-7)**2+(2*(x1)+x2-5)**2
    if flag[0]:
        return (v,)
    return v

PROBLEM = OptimizationProblem(domains= ((-10,10),)*2, objective=__booth__)
