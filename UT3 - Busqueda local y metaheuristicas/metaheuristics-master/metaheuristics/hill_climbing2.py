# -*- coding: utf-8 -*-
import random
import math

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    # if domains ==  ((0,63),)*8 :
    #     return [center[0:i] + (center[i] + d,) + center[i + 1:]
    #                for i in range(len(center)) for d in (-radius, +radius)
    #                if center[i] - radius >= domains[i][0]%64 and center[i] + radius <= domains[i][1]%64
    #            ]
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius)
               if center[i] - d >= domains[i][0] and center[i] + d <= domains[i][1]
           ]
def hill_climbing(problem, steps=100, delta=1, initial=None):
    """ Hill climbing optimization implemented as a generator function.
    """
    current = initial or problem.randomElement() #obtiene una palabra random?
    lastEval = problem.objective(current) #obtiene la distancia entre current y helloworld!
    current = (current, lastEval) # la palabra con su valuacion
    yield current
    for step in range(steps):
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains)) #domains es el dominio de los ascii que son caracteres
        current = nexts[0]
        if problem.compareEvaluations(lastEval, current[1]) > 0:
            lastEval = current[1]
        else:
            break # local optimum has been reached
        yield current

def random_restart_hill_climbing(problem,restarts = 20,steps=100):
    print("Random RESTART")
    simulations=[]
    for i in range(restarts):
        #print(str(i)+" RESTART----")
        for step in hill_climbing(problem, steps):
            imprimir = ' '.join(map(str,step[0]))
        simulations.append(step)
        print("Simulation #{}, Value: {} , Distance: {}".format(str(i),imprimir,str(step[1])))
        # if (step[1]==0):
        #         return min(simulations,key=lambda x:x[1])
    return min(simulations,key=lambda x: abs(x[1]))


def test1(problem=None,restarts=10,steps=100):
    if not problem:
        from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6
        problem=BUKING_N6
        #problem = hello_world()
        #problem = SCHAFFER_N2
    result = random_restart_hill_climbing(problem,restarts,steps)
    print(result)
def test2():
    from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6,ALFILES
    print("\nTest ALFILES")
    result = test1(problem=ALFILES,steps=1000000,restarts=1000)
    print(result)
    #print(showBoard(result))
    print("\nTest Hello World")
    #test1(problem=hello_world())
    print("\nTest SCHAFFER_N2")
    #test1(problem=SCHAFFER_N2)
    print("\nTest BUKING_N6")
    #test1(problem=BUKING_N6)
