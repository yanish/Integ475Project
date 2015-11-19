import metaknowledge as mk
import networkx as Nx
import os
os.chdir("/Users/Yanish/Documents/Fall_2015/Integ_475/mini_project_2/Integ475Project")

RC = mk.RecordCollection ("/Users/Yanish/Documents/Fall_2015/Integ_475/mini_project_2/Integ475Project/data/")
coAuth = RC.coAuthNetwork()
Net = RC.coCiteNetwork()
Net=mk.drop_edges(Net, minWeight=3)
Nx.write_graphml(Net, "/Users/Yanish/Documents/Fall_2015/Integ_475/mini_project_2/Integ475Project/networks/net.graphml")
