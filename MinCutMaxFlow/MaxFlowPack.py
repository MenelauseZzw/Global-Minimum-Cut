from MinCutWagner.CreateGraph import CreateGraph
import numpy as np

def compute_res_graph(res_Graph,path,s,t):
    vv = t
    flow = []
    while vv != s:
        v1 = path[vv]
        f = res_Graph.graph[v1,vv]
        flow.append(f)
        vv = v1
    minf = np.min(np.array(flow))

    #recompute the res_Graph
    vv = t
    while vv != s:
        v1 = path[vv]
        res_Graph.graph[v1,vv] -= minf
        res_Graph.graph[vv,v1] += minf
        vv = v1

    return minf

def FindAugmentingPath(res_Graph,s,t,path):
    V_num = len(res_Graph.V)
    queue = []
    isfind = False
    flag = np.zeros(V_num)
    queue.append(s)
    flag[s] = 1

    while len(queue) != 0:
        queue.reverse()
        v = queue.pop()
        queue.reverse()
        for nh in np.arange(V_num):
            if res_Graph.graph[v,nh]!=0 and flag[nh]==0:
                if nh==t:
                    path[nh] = v
                    isfind = True
                    break
                else:
                    flag[nh] = 1
                    path[nh] = v
                    queue.append(nh)
        if isfind ==True:
            return True

    return False

def Maxflow(graph_capacity,s,t):
    V_num = len(graph_capacity.V)
    res_graph = CreateGraph(V_num)
    res_graph.graph = graph_capacity.graph.copy()
    path = [None for i in np.arange(V_num)]
    maxflow = 0
    while FindAugmentingPath(res_graph,s,t,path):
        maxflow += compute_res_graph(res_graph,path,s,t)
        path = [None for i in np.arange(V_num)]

    return maxflow,res_graph

def findmincut(graph_capacity,res_Graph,s):
    V_num = len(graph_capacity.V)
    queue = []
    queue.append(s)
    flag = [False for i in np.arange(V_num)]
    flag[s] = True
    S = []
    S.append(s)

    while len(queue) != 0:
        queue.reverse()
        v = queue.pop()
        queue.reverse()
        for nh in np.arange(V_num):
            if res_Graph.graph[v,nh]!=0 and flag[nh]==False:
                S.append(nh)
                flag[nh] = True
                queue.append(nh)
    T = [v for v in graph_capacity.V if v not in S]

    return S,T

if __name__ == "__main__":
    graph_capcity = CreateGraph(6)
    graph_capcity.graph = np.array([[0,10,3,1,0,0],
                      [0,0,1,0,2,5],
                      [0,0,0,0,6,0],
                      [0,0,3,0,3,10],
                      [0,0,0,0,0,5],
                      [0,0,0,0,0,0]])
    '''graph_capcity.graph = np.array([[0,100,100,0],
                                    [0,0,1,100],
                                    [0,0,0,100],
                                    [0,0,0,0]])'''
    maxflow,res_graph = Maxflow(graph_capcity,0,5)
    print(maxflow)
    (S,T) = findmincut(graph_capcity,res_graph,0)
    print(S,T)