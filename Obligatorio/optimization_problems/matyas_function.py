from math import *
from problem import OptimizationProblem
import random

flag=[True]
acc=[0]
def __matyas__(elem):
    elem=list(elem)
    acc[0]+=1
    (x,y)=elem
    v = 0.26*(x**2+y**2)-0.48*(x*y)
    if flag[0]:
        return (v,)
    return v
PROBLEM = OptimizationProblem(domains= ((-10,10),)*2, objective=__matyas__)
