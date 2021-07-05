#selecting 5 graph

from Question1 import Graphdetail
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def plotting_graph(name):
    header_list = ["a","b","w"]
    E = pd.read_csv (name, sep= " ", header=None, names = header_list)
    graph = nx.from_pandas_edgelist(E, "a","b",["w"])
    degrees = graph.degree()
    new_tuple = []
    x_cord,y_cord = [],[]
    for i ,j in degrees:
        if j not in x_cord:
            x_cord.append(j)
    for i in x_cord:
        count = 0
        for j,k in degrees:
            if k == i:
                count = count+1
        else:
            y_cord.append(count/graph.number_of_nodes())
    for i,j in zip(x_cord,y_cord):
         new_tuple.append((i,j))
    new_tuple.sort(key=lambda x:x[0])
    plt.plot(*zip(*new_tuple))
    plt.show()


graph2 = Graphdetail("aves-barn-swallow-contact-network.edges")
plotting_graph("aves-barn-swallow-contact-network.edges")
graph3 = Graphdetail("bio-CE-HT.edges")
plotting_graph("bio-CE-HT.edges")
graph4 = Graphdetail("bio-SC-TS.edges")
plotting_graph("bio-SC-TS.edges")
graph5 = Graphdetail("insecta-ant-colony6-day29.edges")
plotting_graph("insecta-ant-colony6-day29.edges")
graph6 = Graphdetail("mammalia-voles-rob-trapping.edges")
plotting_graph("mammalia-voles-rob-trapping.edges")
