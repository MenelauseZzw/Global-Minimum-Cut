from MinCutMaxFlow.MaxFlowPack import *
from MinCutWagner.CreateGraph import CreateGraph
import numpy as np

def MaxMinCut(Graph,source):
    V = Graph.V
    mincut = []
    mincutset = []
    for v in V:
        if v != source:
            graph_copy  = CreateGraph(len(V))
            graph_copy.graph = Graph.graph.copy()
            s = source
            #t = np.random.choice(V[v+1:],1)[0]
            t = v
            mf,residualG = Maxflow(graph_copy,s,t)
            mcut = findmincut(graph_copy,residualG,s)
            mincut.append(mf)
            mincutset.append(mcut)
    min_index = np.argsort(mincut)[0]
    return mincut[min_index],mincutset[min_index]

if __name__ == "__main__":
    graph = CreateGraph(8)
    edges = {"1-2":2,"1-5":3,"2-5":2,"2-6":2,"5-6":3,"2-3":3,"6-7":1,"3-7":2,
             "3-4":4,"4-7":2,"7-8":3,"4-8":2}
    graph.addedge(edges)
    print(MaxMinCut(graph,0))