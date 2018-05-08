import random
import math
import optimization_problem as o
def surroundings(center, radius, domains):
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius)
               if center[i] - radius >= domains[i][0] and center[i] + radius <= domains[i][1]
           ]

def tabu_search(problem,tabuList_size=1000,steps=1000,delta=1 ):
    stopCondition = False
    s_best = problem.randomElement();
    s_best = (s_best,problem.objective(s_best))
    tabu_list =[]
    while (not stopCondition):
        steps=steps-1
        candidate_list=[]
        neighborhood = surroundings(s_best[0], delta, problem.domains)
        if neighborhood==[]:
            stopCondition=True
            break;
        for candidate in neighborhood:
            if candidate not in tabu_list:
                candidate_list.append(candidate)
        candidate = problem.evaluated(candidate_list)[0]
        if(problem.evaluate(candidate[0])<=problem.evaluate(s_best[0])):
            s_best=candidate
            tabu_list.append(candidate)
            #Metodo estandar para quitar valores de tabu
            tabu_list=expire_features(tabu_list,tabuList_size)
        if steps<0:
            stopCondition=True
    return s_best

def expire_features(tabu_list,tabuList_size):
    while(len(tabu_list)>tabuList_size):
        tabu_list = tabu_list[1:]
    return tabu_list

def test1(s=100,x=100):
    print(tabu_search(o.SCHAFFER_N2,steps=s,tabuList_size=x))
