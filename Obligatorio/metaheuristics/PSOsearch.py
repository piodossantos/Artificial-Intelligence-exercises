import random
import operator
import numpy
from math import *
from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

def generate(size, pmin, pmax, smin, smax):
#	part = creator.Particle(random.uniform(pmin, pmax) for _ in range(size))
	part = creator.Particle(random.randint(pmin,pmax) for _ in range(size))
	part.speed = [random.uniform(smin, smax) for _ in range(size)]
	part.smin = smin
	part.smax = smax
	return part

def updateParticle(part, best, phi1, phi2):
	u1 = (random.uniform(0, phi1) for _ in range(len(part)))
	u2 = (random.uniform(0, phi2) for _ in range(len(part)))
	v_u1 = map(operator.mul, u1, map(operator.sub, part.best, part))
	v_u2 = map(operator.mul, u2, map(operator.sub, best, part))
	part.speed = list(map(operator.add, part.speed, map(operator.add, v_u1, v_u2)))
	for i, speed in enumerate(part.speed):
		if speed < part.smin:
			part.speed[i] = part.smin
		elif speed > part.smax:
			part.speed[i] = part.smax
		part[:] = list(map(operator.add, part, part.speed))


def PSO_search(evaluate=benchmarks.h1,minimax=(1.0,),size=2,pmin=-6,pmax=6,smin=-3,smax=3,GEN=50):
	creator.create("FitnessMinMax", base.Fitness, weights=minimax)
	creator.create("Particle", list, fitness=creator.FitnessMinMax, speed=list,smin=None, smax=None, best=None)
	toolbox = base.Toolbox()
	toolbox.register("particle", generate, size, pmin, pmax, smin, smax)
	toolbox.register("population", tools.initRepeat, list, toolbox.particle)
	toolbox.register("update", updateParticle, phi1=2.0, phi2=2.0)
	toolbox.register("evaluate", evaluate)
	pop = toolbox.population(n=10)
	stats = tools.Statistics(lambda ind: ind.fitness.values)
	best = None
	for g in range(GEN):
		for part in pop:
			part.fitness.values = toolbox.evaluate(part)
			if not part.best or part.best.fitness < part.fitness:
				part.best = creator.Particle(part)
				part.best.fitness.values = part.fitness.values
			if not best or best.fitness < part.fitness:
				best = creator.Particle(part)
				best.fitness.values = part.fitness.values
		for part in pop:
			toolbox.update(part, best)

	return(best,best.fitness.values)
	# return pop, logbook, best

def PSO_adaptor(problem,gen=50):
	# assigned parameters
	pmin = problem.domains[0][0]
	pmax = problem.domains[0][1]
	size = len(problem.domains)
	#size=2
	evaluate = problem.objective
	smin =-abs(pmax - pmin)
	smax = abs(pmax - pmin)
	minimax = (-1.0,)
	if problem.target == inf:
		minimax = (1.0,)

	return PSO_search(evaluate,minimax,size,pmin,pmax,smin,smax,gen)
