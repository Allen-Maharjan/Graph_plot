import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import string
import pandas as pd
from statistics import mean
import scipy
class Graphdetail():

    def __init__(self,name):
            header_list = ["a","b","w"]
            E = pd.read_csv (name, sep= " ", header=None, names = header_list)
            graph = nx.from_pandas_edgelist(E, "a","b",["w"])
            print(f"The number of nodes of the given grahh is {graph.number_of_nodes()}\nThe number of edges of the given graph is {graph.number_of_edges()}")
            self._average_degree(graph.degree())
            self._density(graph.number_of_edges(),graph.number_of_nodes())
            print("The diameter of the given graph is ",self._diameter(graph.edges()))
            print("The clustering coefficient of the graph is ",self._clustering(graph),"\n\n")
            # clustering(graph)
            nx.draw(graph)
            plt.show()

    def _average_degree(self,degree):
        filter_degree = []
        for i in degree:
            filter_degree.append(i[1])
        print(f"The average degree of the graph is :{(sum(filter_degree)/len(filter_degree))}")

    def _density(slef,edges,nodes):
        if nodes <1:
            return 0
        else:
            D = (2*edges)/(nodes*(nodes-1))
            print("The Density of the graph is:",D)

    def _diameter(self,edges):
        temp = list(edges)
        BFS_dict = dict()
        temp_list = []
        for i,j in edges:
            for l,m in edges:
                if (i==l):
                    temp_list.append(m)
            else:
                BFS_dict[i] = temp_list
                temp_list = []
        # print(BFS_dict)
        traverse = self._BFS_graph(BFS_dict,temp[0][0])
        for i in BFS_dict:
            if (traverse[-1] in BFS_dict[i]):
                a = i
                break
        return len((self._BFS_graph(BFS_dict,a)))+1


    def _BFS_graph(self,graph,start):
        visited = []
        queue = [start]
        neighbours = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                if node in graph:
                    neighbours = graph[node]

                for i in neighbours:
                    queue.append(i)
        return(visited)

    def _clustering(self,graph):
        temp_list = []
        clustering_list = []
        for i in graph:
            count = 0
            a = list(graph.neighbors(i))
            for j in a :
                for k in a:
                    if j in graph.neighbors(k):
                        count +=1
            temp_list.append([count/2,len(a)])
        for i,j in temp_list:
            if j > 1:
                clustering_list.append(float((2*i)/(j*(j-1))))
            else:
                clustering_list.append(0)
        return float(mean(clustering_list))


if __name__ == '__main__':
    graph1 = Graphdetail("aves-weaver-social-09.edges")
