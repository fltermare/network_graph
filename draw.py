import networkx as nx
import matplotlib.pyplot as plt
import sys
import os

def draw_graph(graph):
    # extract nodes from graph
    nodes = set([n1 for n1, n2, n3 in graph] + [n2 for n1, n2, n3 in graph])
    print(len(nodes))

    # create networkx graph
    G=nx.Graph()

    # add nodes
    #for node in nodes:
    #    G.add_node(node)
    G.add_nodes_from(nodes)

    # add edges

    for edge in graph:
        G.add_edge(edge[0], edge[1], weight=int(edge[2]))

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 5]

    d = nx.degree(G)


    # draw graph
    pos = nx.spring_layout(G)

    labels = {}
    for node in G.nodes():
        if G.degree(node) > 50:
            labels[node] = node
    #nx.draw(G, with_labels=False)
    #nx.draw_networkx_labels(G, pos, labels, font_size=1)

    nx.draw_networkx_nodes(G, pos, nodelist=d.keys(), node_size=[v*0.05 for v in d.values()], node_color='red')
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width = 0.1, edge_color='b')
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width = 0.01, alpha=0.5, edge_color='b', style='dashed')
    nx.draw_networkx_labels(G, pos, labels, font_size=5, font_color='g')



    #nx.draw(G, pos)

    #nx.draw_random(G)

    plt.axis('off')
    #plt.show()
    # show graph
    plt.savefig("./name.png", dpi=1000, format="png")
    #plt.savefig("./name.png")
    print("done")


def getdata(infile):
    print(infile)
    graph = []
    with open(infile, 'r') as f:
        for line in f:
            if 'flag' in line:
                items = line.strip().split(',')
                graph.append((items[1], items[2], items[8]))
    #print(graph)
    return graph


def main():
    infile = sys.argv[1]
    g = getdata(infile)
    #for i in g:
    #    print(i)
    # draw example
    #graph = [(20, 21),(21, 22),(22, 23), (23, 24),(24, 25), (25, 20)]
    draw_graph(g)

if __name__ == "__main__":
    main()
