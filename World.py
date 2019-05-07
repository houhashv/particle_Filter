import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from Ploter import Ploter


class World:

    def __init__(self, world_size=100):

        self._ploter = Ploter()
        self.world_size = world_size
        self.landmarks = [(20.0, 20.0), (80.0, 80.0), (20.0, 80.0), (80.0, 20.0)]

    def plot(self, show=True):

        fig = plt.figure()
        plt.rcParams.update({'font.size': 16})
        plt.plot([x[0] for x in self.landmarks], [x[1] for x in self.landmarks], "ko")
        self._ploter.config_plot(plt, self.world_size)
        ax = fig.gca()
        ax.set_aspect("equal")
        for i, m in enumerate(["m1", "m2", "m3", "m4"]):
            plt.text(self.landmarks[i][0] - 3, self.landmarks[i][1] + 3, m, fontsize=11)
        if show:
            plt.show()

    def get_world_size(self):

        return self.world_size

    def get_landmarks(self):

        return self.landmarks