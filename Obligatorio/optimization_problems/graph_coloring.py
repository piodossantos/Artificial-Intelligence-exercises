from math import *
from problem import OptimizationProblem
import random

acc=[0]
edges_list = []
def __graph_coloring__(elem):
    acc[0]+=1
    elem=list(elem)
    result=0
    edges = edges_list
    color_list=list(elem)
    for pos in range(len(color_list)):
        current_color = color_list[pos]
        for c in child(pos,edges):
            if color_list[c]==current_color:
                result+=1
    return result
def child(node,edges):
    print(edges)
    return [y for (x,y) in edges if x==node]
def genRandomGraph(n_edges,n_nodes):
    edges=[]
    for i in range(n_nodes):
        elem = (i,random.randint(0,n_nodes-1))
        if elem[0]!=elem[1]:
            if elem not in edges:
                edges.append(elem)
                edges.append((elem[1],elem[0]))
    while(len(edges)<n_edges*2):
        elem = (random.randint(0,n_nodes-1),random.randint(0,n_nodes-1))
        if elem[0]!=elem[1]:
            if elem not in edges:
                edges.append(elem)
                edges.append((elem[1],elem[0]))
    return edges
def graph_coloring_problem(n_nodes,n_edges,n_colors):
    #edges_list.append(genRandomGraph(n_edges,n_nodes))
    for elem in genRandomGraph(n_edges,n_nodes):
        edges_list.append(elem)
    return OptimizationProblem(domains= ((0,n_colors-1),)*n_nodes, objective=__graph_coloring__)
PROBLEM = graph_coloring_problem(15,40,15)
