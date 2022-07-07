## CSDL, POSTECH, Korea Summer Internship 2022
## Original file created by Minjae Kim
## kmj0824@postech.ac.kr


import random
import numpy as np

random.seed(300)


class Cell:
    def __init__(self, cell_id, degree):
        self.id = int(cell_id) - 1
        self.coordinate = np.array([random.randint(0, 1000) / 10, random.randint(0, 1000) / 10])
        self.degree = int(degree)
        self.connected_nets = []


class Pad:
    def __init__(self, pad_id, connected_net, x, y):
        self.pad_id = int(pad_id) - 1
        self.coordinate = np.array([x, y])
        self.connected_net = int(connected_net) - 1


class Net:
    def __init__(self, net_id):
        self.net_id = int(net_id)
        self.connected_cells = []
        self.connected_pad = []
