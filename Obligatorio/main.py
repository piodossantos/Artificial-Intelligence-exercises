from metaheuristics import PSOsearch as pso,tabusearch as tabu
from optimization_problems import booth_function as booth, graph_coloring as gc, matyas_function as matyas
import numpy as np


__logs__=[]

def experiment(steps=100):
    run_simulations(steps)
    generate_stats()

###Esta funcion se encarga de correr todas las simulaciones y almacenar los resultados en los logs
def run_simulations(steps=100):
    for (metaheuristic,m_name,flag) in [(tabu.tabu_search,"tabu",False),(pso.PSO_adaptor,"PSO",True)]:
        for (problem,p_name) in [(booth,"booth"),(gc,"graph"),(matyas,"matyas")]:
            create_log(problem,metaheuristic,flag,m_name+"-"+p_name+".csv",steps)
            #create_log(booth,tabu.tabu_search,"tabu.csv")

###Esta funcion se encarga de corres las simulaciones y guardarlos en un log
### -problem, Representacion del problema
### -metaheuristica, que se usa para evaluar
### -flag, control para el valor de retorno de las funciones de evaluacion
### -path, la ruta donde almacenaran los resultados
### -steps, la cantidad de simulaciones que va a almacenar
def create_log(problem=None,metaheuristic=None,flag=False,path="/default.csv", steps=100):
    if metaheuristic==None or problem==None:
        return ("Error")
    log=""
    problem.flag[0]=flag
    for _ in range(steps):
        problem.acc[0]=0
        (sol,dist)=metaheuristic(problem.PROBLEM)
        if flag:
            dist=dist[0]
        val=(problem.acc[0],dist)
        log+=(str(problem.acc[0])+","+str(dist)+'\n')
    f = open(path,"w")
    #f.write("#Evaluation,#Solution\n")
    f.write(log)
    print("Create file: "+path)
    __logs__.append(path)
    f.close()
### Esta funcion se encarga de generar datos sobre los valores almacenados
### -files_path, nombre de archivos que usara para generar los datos
def generate_stats(files_path=__logs__):
    log="\n\n-----------------------------\n\n"
    for path in files_path:
        acc=[]
        dist=[]
        log+="File: "+path+"\n\n"
        f=open(path,"r")
        first_line=True
        for line in f:
            if first_line:
                first_line=False
            else:
                temp=line.split(',')
                acc.append(float(temp[0]))
                dist.append(float(temp[1]))

        for (a,b) in [(np.array(acc),"\nEvaluation\n"),(np.array(dist),"\nSolution\n")]:
            log+=b+"\n"
            log+="Mean: "+str(a.mean())+"\n"
            log+="std: "+str(a.std())+"\n"
            log+="Median: "+str(np.median(a))+"\n"
            log+="Max: "+str(a.max())+"\n"
            log+="Min: "+str(a.min())+"\n"
        log+="\n\n-----------------------------\n\n"
        f.close()
    print(log)
