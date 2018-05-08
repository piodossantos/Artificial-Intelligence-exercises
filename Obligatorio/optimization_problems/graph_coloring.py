from math import *
from problem import OptimizationProblem
import random

edges_list =[[]]
def __graph_coloring__(elem):
    result=0
    edges = edges_list[0]
    color_list=list(elem)
    for pos in range(len(color_list)):
        current_color = color_list[pos]
        for c in child(pos,edges):
            if color_list[c]==current_color:
                result+=1
    return result

def child(node,edges):
    return [y for (x,y) in edges if x==node]
def genRandomGraph(n_edges,n_nodes):
    edges=[]
    while(len(edges)<n_edges):
        elem = (random.randint(0,n_nodes-1),random.randint(0,n_nodes-1))
        if elem[0]!=elem[1]:
            if elem not in edges:
                edges.append(elem)
    return edges
def graph_coloring_problem(n_nodes,n_edges,n_colors):
    edges_list[0]=[genRandomGraph(n_edges,n_nodes)]
    return OptimizationProblem(domains= ((0,n_colors-1),)*n_nodes, objective=__graph_coloring__)
