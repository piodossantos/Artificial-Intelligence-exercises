# -*- coding: utf-8 -*-
import random
import math

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
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
		
def restart_hill_climbing(problem,restarts = 20,steps=100):
	for i in range(restarts):
		print(str(i)+" RESTART----")
		for step in hill_climbing(problem, steps):
			imprimir = ''.join(map(chr,step[0]))
		print(imprimir)
		if (step[1]==0):
				return

#T es la temperatura con la que empieza luego va bajando, M la cantidad que quiero que itere y Tf la temperatura final
def temple_simulado(problema,T,Tf=0.1,M=100, delta=1, initial=None): 
	current = initial or problem.randomElement() #obtiene una palabra random?
    lastEval = problem.objective(current) #obtiene la distancia entre current y helloworld! 
    current = (current, lastEval) # la palabra con su valuacion
    yield current
	beta = (T-Tf)/(M*T*Tf) # cte que se calcula para aplicar Cauchy modificado para que itere M veces
	Tk = T
	while Tk > Tf:
		#domains es el dominio de los ascii que son caracteres y evalueated los evalua con valores absolutos segun el problema
		nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
		nextChangeFlg = False
        while(!nextChangeFlg):
			# current = nexts[0] cualquier sucesor
			current = nexts.pop(random.randint(0,len(nexts)-1))
			if (problem.compareEvaluations(lastEval, current[1]) > 0):
				lastEval = current[1]
				nextChangeFlg = True
			else:
				# calcular probabilidad
				diferencia = lastEval - current[1]
				if (math.exp(diferencia/Tk)*100 <= random.randint(0,100)):
					lastEval = current[1]
					nextChangeFlg = True
		#bajo el Tk
		Tk = enfriamientoCauchyM(Tk,beta)
		yield current
		
def enfriamientoCauchyM(Tk,beta):#enfria T con Cauchy modificado para que itere M veces
	return Tk/(1+beta*Tk) 

def test1(problem=None,restarts=20,steps=100):
	if not problem:
		from .test_problems import hello_world
		problem = hello_world()

	restart_hill_climbing(problem,restarts,steps)
	# for step in hill_climbing(problem, steps=1000):
		# print(step, ''.join(map(chr, step[0])))
