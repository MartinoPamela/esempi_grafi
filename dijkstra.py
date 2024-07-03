import networkx as nx
import matplotlib.pyplot as plt
import random

#building graph
G = nx.directed_havel_hakimi_graph([3] * 15,
                                   [3] * 15,
                                   create_using=None)
# è un grafo che è già fornito dalla libreria, havel_hakimi è una particolare struttura a grafo
# in cui posso assegnare la dimensionalità dei nodi, quindi gli passo come parametro due liste,
# in particolare gli sto dicendo che ha 15 nodi che hanno in degree = 3 quindi 3 archi entranti
# e hanno tre archi uscenti, e poi gli assegna dei pesi randomici

for e in G.edges():
    G[e[0]][e[1]]['weight'] = random.randrange(1,10)


print(G.nodes())
print(G.edges())

#getting shortest path
print(nx.dijkstra_path(G, 0, 8))  # mi dà direttamente il percorso, mi dà una lista di nodi
print(nx.dijkstra_path_length(G, 0, 7))  # implementazione che mi dà la lunghezza,
# qui gli sto già assegnando anche un target

optpath = nx.dijkstra_path(G, 0, 7)
optedges = []
for i in range(0, len(optpath)-1):
    optedges.append([optpath[i], optpath[i+1],  G[optpath[i]][optpath[i+1]]['weight']])


##plotting
pos=nx.spring_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

nx.draw_networkx_edges(G, pos, optedges, edge_color="red")

plt.savefig("plot")
plt.show()