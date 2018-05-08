from math import *
from problem import OptimizationProblem
import random

acc=[0]
def __matyas__(elem):
    acc[0]+=1
    (x,y)=elem
    return 0.26*(x**2+y**2)-0.48*(x*y)

PROBLEM = OptimizationProblem(domains= ((-10,10),)*2, objective=__matyas__)
