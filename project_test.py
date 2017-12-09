from MinCutWagner.Stoer_Wagner_mincut import *
from MinCutMaxFlow.MaxMincut import *

#constructing the graph
numberofV = 6 #specify the number of vertices in your graph
#construct the edges by dictionary
edges = {"1-2":1,"1-4":3,"1-5":3,"2-3":5,"2-4":1,"2-5":1,"2-6":7,"3-4":6,
        "3-5":7,"3-6":1,"4-5":1,"5-6":3}
start = 0 #specify the start point

################## The Test #####################

#implementation of the MaxMincut algorithm
graph = CreateGraph(numberofV)
graph.addedge(edges)
mincut_maxmin = MaxMinCut(graph,start)
print("mincut by MaxMincut algorithm: %d" %mincut_maxmin[0])

#implementation of the StoerWagnermincut algorithm
graph = CreateGraph(numberofV)
graph.addedge(edges)
mincut_wagner = MinCut(graph,start)
print("mincut by StoerWagnermincut algorithm: %d" %mincut_wagner)