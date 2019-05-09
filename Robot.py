import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
from Ploter import Ploter


class Robot:

    def __init__(self, world_size=100):

        self._ploter = Ploter()
        self._world_size = world_size
        # pose
        self.x = np.random.rand() * self._world_size
        self.y = np.random.rand() * self._world_size
        self.theta = np.random.rand() * 2 * np.pi

        # noise
        self.forward_noise = 0
        self.turn_noise = 0
        self.sense_distance_noise = 0

    def set(self, new_x, new_y, new_orientation):

        if new_x < 0 or new_x >= self._world_size:
            raise Exception('X coordinate out of bound')

        if new_y < 0 or new_y >= self._world_size:
            raise Exception('Y coordinate out of bound')

        if new_orientation < 0.0 or new_orientation >= 2 * np.pi:
            Exception('Orientation must be in [0,2pi]')

        self.x = new_x
        self.y = new_y
        self.theta = new_orientation

    def print(self):

        print('[x= {} y={} heading={}]'.format(self.x, self.y, self.theta))

    def plot(self, mycolor="b", style="robot", show=True):

        if style == "robot":

            phi = np.linspace(0, 2 * np.pi, 101)
            r = 1
            # plot robot body
            plt.plot(self.x + r * np.cos(phi), self.y + r * np.sin(phi), mycolor)
            # plot heading direction
            plt.plot([self.x, self.x + r * np.cos(self.theta)], [self.y, self.y + r * np.sin(self.theta)], mycolor)

        elif style == "particle":
            plt.plot(self.x, self.y, '.', mycolor)
        else:
            print("unknown style")

        if show:
            plt.show()

    def set_noise(self, new_forward_noise, new_turn_noise, new_sensing_distance_noise):

        self.forward_noise = new_forward_noise
        self.turn_noise = new_turn_noise
        self.sense_distance_noise = new_sensing_distance_noise

    def move(self, u1, u2, meu_u1=0, meu_u2=0, noise=True):

        if noise:
            u1_noise = np.random.normal(meu_u1, self.turn_noise)
            u2_noise = np.random.normal(meu_u2, self.forward_noise)
        else:
            u1_noise = 0
            u2_noise = 0

        self.theta = int(10 * (self.theta + u1 + u1_noise)) / 10
        self.x = int(10 * (self.x + (u2 + u2_noise) * np.cos(self.theta))) / 10
        self.y = int(10 * (self.y + (u2 + u2_noise) * np.sin(self.theta))) / 10

        if self.x > self._world_size:
            while(self.x > self._world_size):
                self.x = self.x - 100
        elif self.x < 0:
            while(self.x < 0):
                self.x = self.x + 100
        if self.y > self._world_size:
            while (self.y > self._world_size):
                self.y = self.y - 100
        elif self.y < 0:
            while (self.y < 0):
                self.y = self.y + 100

        return self.x, self.y, self.theta

    def sense(self, m):

        meu = 0
        landmarks = np.asarray(m.get_landmarks())
        location = np.asarray([(self.x, self.y) for i in range(len(landmarks))])
        return list(map(lambda x, y: np.linalg.norm(x - y) + np.random.normal(meu, self.sense_distance_noise),
                        landmarks, location))

    def measurement_probability(self, f, c, x=None, m=None):

        q = 1
        for c in range(len(f)):
            i = c
            r = np.linalg.norm(np.asarray(m.get_landmarks()[i]) - np.asarray((self.x, self.y)))
            # phi = np.arctan2(m.get_landmarks()[i][1] - self.y, m.get_landmarks()[i][0] - self.x)
            q *= norm.pdf(f[i] - r, 0, self.sense_distance_noise)
        return q

    def get_pose(self):

        return self.x, self.y, self.theta

    def straight_line(self, actions, noise=False, show=True):

        poses = [self.get_pose()]

        for action in actions:
            self.move(action[0], action[1], noise=noise)
            poses.append(self.get_pose())

        self.plotint(poses, noise, show)

        return poses

    def plotint(self, poses, noise, show):

        fig = plt.figure()
        plt.rcParams.update({'font.size': 16})
        if noise:
            plt.plot([x[0] for x in poses], [x[1] for x in poses], dashes=[6, 2])
        else:
            plt.plot([x[0] for x in poses], [x[1] for x in poses])
        self._ploter.config_plot(plt, self._world_size)
        times = ["time {}".format(i) for i in range(len(poses))]
        for i, m in enumerate(times):
            plt.text(poses[i][0] - 3, poses[i][1] + 3, m, fontsize=11)
        ax = fig.gca()
        ax.set_aspect("equal")
        if show:
            plt.show()
