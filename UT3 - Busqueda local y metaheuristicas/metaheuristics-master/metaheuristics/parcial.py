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
               if center[i] - radius >= domains[i][0] and center[i] + radius <= domains[i][1]
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

def random_restart_hill_climbing(problem,restarts = 20,steps=100,maxmin=0):
    print("Random RESTART")
    simulations=[]
    for i in range(restarts):
        for step in hill_climbing(problem, steps):
            imprimir = ' '.join(map(str,step[0]))
        simulations.append(step)
        print("Simulation #{}, Value: {} , Distance: {}".format(str(i),imprimir,str(step[1])))
    if maxmin>0:
        return max(simulations,key=lambda x: x[1])
    return min(simulations,key=lambda x: x[1])
#T es la temperatura con la que empieza luego va bajando, M la cantidad que quiero que itere y Tf la temperatura final
def temple_simulado(problem,T=30,Tf=0.5,M=15, delta=1, initial=None):
    current = initial or problem.randomElement() #obtiene una palabra random?
    lastEval = problem.objective(current) #obtiene la distancia entre current y helloworld!
    current = (current, lastEval) # la palabra con su valuacion
    yield current
    beta = (T-Tf)/(M*T*Tf) # cte que se calcula para aplicar Cauchy modificado para que itere M veces
    Tk = T
    while Tk > Tf:
        #print(str(Tk))
		#domains es el dominio de los ascii que son caracteres y evalueated los evalua con valores absolutos segun el problema
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        nextChangeFlg = False
        while(not nextChangeFlg):
            if len(nexts)==0:
                break
            current = nexts.pop(random.randint(0,len(nexts)-1))
            if (problem.compareEvaluations(lastEval, current[1]) > 0):
                lastEval = current[1]
                nextChangeFlg = True
            else:
				# calcular probabilidad
                diferencia = lastEval - current[1]
                if diferencia ==0:
                    yield current
                    return
                if (math.exp(diferencia/Tk)*100 >= random.randint(0,100)):
                    lastEval = current[1]
                    nextChangeFlg = True

		#bajo el Tk
        temp=Tk
        Tk = enfriamientoCauchyM(Tk,beta)
        #print("Tk prev: {}\t Tk posterior: {} \tVariacion: {}".format(temp,Tk,temp/Tk))
        yield current

def enfriamientoCauchyM(Tk,beta):#enfria T con Cauchy modificado para que itere M veces
	return Tk/(1+beta*Tk)
#Llama a temple simulado
def test3(problem=None,T=10,Tf=0.5,M=10):
    if not problem:
        from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6
        problem=hello_world()
    #return temple_simulado(problem,M=1000)
    for step in temple_simulado(problem,T=T,Tf=Tf,M=M):
        imprimir = ' '.join(map(str,step[0]))
    #print(imprimir)
    return step
#usar este para correr todas las operaciones con temple simulado
def testTS():
    from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6,ALFILES,BODA
    print("\nTest BODA")
    result = test3(problem=BODA,T=750,Tf=1,M=25000)
    print(result)
    print("\nTest ALFILES")
    result = test3(problem=ALFILES,T=750,Tf=1,M=25000)
    print(result)
    print("\nTest Hello World")
    print(test3(problem=hello_world(),T=75,Tf=0.5,M=2000))
    print("\nTest SCHAFFER_N2")
    print(test3(problem=SCHAFFER_N2,T=15,Tf=0.005,M=10000))
    print("\nTest BUKING_N6")
    print(test3(problem=BUKING_N6,T=5,Tf=0.01,M=10))
#Llama a Random Restart , si queres ejecutar solo hill climbing, entonces restarts=1
def test1(problem=None,restarts=10,steps=100,maxmin=0):
    if not problem:
        from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6
        problem=BUKING_N6
        #problem = hello_world()
        #problem = SCHAFFER_N2
    result = random_restart_hill_climbing(problem,restarts,steps,maxmin)
    print(result)

#ejecuta todos los test con Random Restart
def testRR():
    from .test_problems import hello_world,SCHAFFER_N2,BUKING_N6,ALFILES,BODA
    print("\nTest BODA")
    result = test1(problem=BODA,steps=1000000,restarts=10,maxmin=1)
    print(result)
    print("\nTest ALFILES")
    result = test1(problem=ALFILES,steps=1000000,restarts=10,maxmin=1)
    print(result)
    print("\nTest Hello World")
    test1(problem=hello_world())
    print("\nTest SCHAFFER_N2")
    test1(problem=SCHAFFER_N2)
    print("\nTest BUKING_N6")
    test1(problem=BUKING_N6)
