import sys
sys.path.insert(0, '')
sys.path.extend(['../'])

import numpy as np

from graph import tools

joint_index = {0 : "Nose", 11 : "LShoulder", 12 : "RShoulder", 13 : "LElbow", 
               14 : "RElbow", 15 : "LWrist", 16 : "RWrist", 23 : "LHip", 24 : "RHip", 
               25 : "LKnee", 26 : "RKnee", 27 : "LAnkle", 28 : "RAnkle"}
# {0,  "Nose"}
# {11,  "LShoulder"},
# {12,  "RShoulder"},
# {13,  "LElbow"},
# {14,  "RElbow"},
# {15,  "LWrist"},
# {16,  "RWrist"},
# {23,  "LHip"},
# {24,  "RHip"},
# {25,  "LKnee"},
# {26, "RKnee"},
# {27, "LAnkle"},
# {28, "RAnkle"},

num_node = 13
indexes = list(joint_index.keys())
self_link = [(i , i) for i in indexes]

inward = [(16, 14), (14, 12), (15, 13), (13, 11), (27, 25), (25, 23), 
          (28, 26), (26, 24), (23, 11), (24, 12), (24, 23), (12, 11), (0, 12), (0, 11)]

outward = [(j, i) for (i, j) in inward]

neighbor = inward + outward


class AdjMatrixGraph:
    def __init__(self, *args, **kwargs):
        self.num_nodes = num_node
        self.edges = neighbor
        self.self_loops = [(i, i) for i in range(self.num_nodes)]
        self.A_binary = tools.get_adjacency_matrix(self.edges, self.num_nodes)
        self.A_binary_with_I = tools.get_adjacency_matrix(self.edges + self.self_loops, self.num_nodes)


if __name__ == '__main__':
    graph = AdjMatrixGraph()
    A_binary = graph.A_binary
    import matplotlib.pyplot as plt
    print(A_binary)
    plt.matshow(A_binary)
    plt.show()
