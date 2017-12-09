from CreateGraph import CreateGraph
import numpy as np
import copy

def MinCutPhase(Graph,Vertex):
    A = [Vertex]
    #modify
    Vlist = copy.deepcopy(Graph.V)
    Vlist.remove(Vertex)
    #######

    #modify2
    weightlist = {}
    for v in Vlist:
        weightlist[v] = Graph.graph[v,Vertex]
    while len(A) != len(Graph.V):
        maxw_k = 0
        maxw = 0
        for k,v in weightlist.items():
            if v>maxw:
                maxw = v
                maxw_k = k
        del weightlist[maxw_k]
        for k,v in weightlist.items():
            v += Graph.graph[k,maxw_k]
            weightlist[k] = v
        A.append(maxw_k)
        Vlist.remove(maxw_k)

    ##original & modify 1
    '''while len(A) != len(Graph.V):
        maxw_n = 0
        maxw = 0
        #for i in Vlist:
        for i in Vlist:
            #if i not in A:
            wi = 0
            for v in A:
                w = Graph.graph[v,i]
                wi += w
            if wi > maxw_n:
                maxw_n = wi
                maxw = i
        A.append(maxw)
        Vlist.remove(maxw)'''

    cut_of_phase = np.sum(Graph.graph[A[-1],:])

    #merging the last two vertexes added
    for v,w in enumerate(Graph.graph[A[-1],:]):
        if w != 0 and v != A[-2]:
            Graph.graph[A[-2],v] += w
            Graph.graph[v,A[-2]] += w
        Graph.graph[A[-1],v] = 0
        Graph.graph[v,A[-1]] = 0
    Graph.V.remove(A[-1])
    return cut_of_phase,A

def MinCut(Graph,Vertex):
    minimum = 1e10
    while (len(Graph.V)) > 1:
        cut_of_phase = MinCutPhase(Graph,Vertex)
        if cut_of_phase[0] < minimum:
            minimum = cut_of_phase[0]
    return minimum


if __name__ == "__main__":
    graph = CreateGraph(6)
    edges = {"1-2":1,"1-4":3,"1-5":3,"2-3":5,"2-4":1,"2-5":1,"2-6":7,"3-4":6,
         "3-5":7,"3-6":1,"4-5":1,"5-6":3}
    graph.addedge(edges)
    #MinCutPhase(graph,1)
    for i in np.arange(6):
        graph = CreateGraph(6)
        edges = {"1-2":1,"1-4":3,"1-5":3,"2-3":5,"2-4":1,"2-5":1,"2-6":7,"3-4":6,
         "3-5":7,"3-6":1,"4-5":1,"5-6":3}
        graph.addedge(edges)
        print(MinCut(graph,i))
    #print(MinCut(graph,1))