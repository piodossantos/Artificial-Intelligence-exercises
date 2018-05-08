from metaheuristics import PSOsearch as pso,tabusearch as tabu
from optimization_problems import booth_function as booth , graph_coloring as gc, matyas_function as matyas

def create_log(problem=None,metaheuristic=None,path="/logs.csv", steps=100):
    if metaheuristic==None or problem==None:
        return ("Error")
    log=""
    for _ in range(steps):
        problem.acc[0]=0
        (sol,dist)=metaheuristic(problem.PROBLEM)
        log+=(str(problem.acc[0])+","+str(dist)+'\n')
    f = open(path,"w")
    f.write("#Evaluation,#Solution\n")
    f.write(log)
    f.close()

def test():
    create_log(booth,tabu.tabu_search,"tabu.csv")
def testgraph(n_nodes,n_edges,n_colors):
    gc.acc[0]=0
    problem = gc.graph_coloring_problem(n_nodes,n_edges,n_colors)
    print(tabu.tabu_search(problem,steps=1000,tabuList_size=1000))
def testBooth():
    booth.acc[0]=0
    problem = booth.BOOTH
    print(tabu.tabu_search(problem,steps=1000,tabuList_size=1000))
def testMatyas():
    matyas.acc[0]=0
    problem = matyas.MATYAS
    print(tabu.tabu_search(problem,steps=1000,tabuList_size=1000))
