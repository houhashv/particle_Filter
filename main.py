from Robot import Robot
from World import World
import numpy as np
from ast import literal_eval

def MCL(particles, ut, world):

    X_t = {}
    for particle in particles:
        xt, wt = particle_wt(particle, ut, world)
        if str(xt) in X_t.keys():
            X_t[str(xt)] += wt
        else:
            X_t[str(xt)] = wt

    draws = []
    total_sum = sum(X_t.values())
    measures = np.asarray(sorted(X_t.items(), key=lambda kv: (kv[1], kv[0])))
    M = measures.shape[0]
    rand = np.random.random() / (M - 1)
    for m in range(0, M):
        accumulate = float(measures[0][1]) / total_sum
        i = 0
        U = rand + m / (M - 1)
        while U > accumulate:
            i += 1
            try:
                accumulate += float(measures[i][1]) / total_sum
            except:
                break
        pose = literal_eval(measures[i - 1][0])
        draws.append(pose)

    x = np.mean([x[0] for x in draws])
    y = np.mean([x[1] for x in draws])
    theta = np.mean([x[2] for x in draws])
    pose = (x, y, theta)

    return pose, draws

def particle_wt (X_t, ut, world):

    robot = Robot()
    robot.set(X_t[0], X_t[1], X_t[2])
    robot.set_noise(5, 0.1, 5)
    xt = robot.move(ut[0], ut[1])
    zt = robot.sense(world)
    wt = robot.measurement_probability(zt, 0, None, world)
    return xt, wt

if __name__ == "__main__":

    world = World()
    # world.plot()
    robot1 = Robot()
    robot1.set_noise(5, 0.1, 5)
    robot2 = Robot()
    robot2.set_noise(5, 0.1, 5)
    robot3 = Robot()
    robot3.set_noise(5, 0.1, 5)
    # a
    poses = [(40, 40, 0), (60, 50, np.pi / 2), (30, 70, 3 * np.pi / 4)]
    # a - robot 1
    robot1.set(poses[0][0], poses[0][1], poses[0][2])
    world.plot(False)
    robot1.plot()
    robot1.print()
    # a - robot 2
    robot2.set(poses[1][0], poses[1][1], poses[1][2])
    world.plot(False)
    robot2.plot()
    robot2.print()
    # a - robot 3
    robot3.set(poses[2][0], poses[2][1], poses[2][2])
    world.plot(False)
    robot3.plot()
    robot3.print()
    # b - implemented in robot class
    # c - implemented in robot class
    # d - implemented in robot class
    measurements = robot1.sense(world)
    actions = [(0, 60),
               (np.pi / 3, 30),
               (np.pi / 4, 30),
               (np.pi / 4, 20),
               (np.pi / 4, 40)]
    # e

    robot = Robot()
    robot.set_noise(5, 0.1, 5)
    robot.set(10, 15, 0)
    no_noise_poses = robot.straight_line(actions, False, False, False)
    # f
    robot = Robot()
    robot.set_noise(5, 0.1, 5)
    robot.set(10, 15, 0)
    real_poses = robot.straight_line(actions, True, False, True)
    # g
    num_of_particales = 1000
    X_t_1 = (10, 15, 0)
    results = [X_t_1]
    particles = np.tile(X_t_1, (num_of_particales, 1))

    for ut in actions:
        pose, particles = MCL(particles, ut, world)
        results.append(pose)

    robot = Robot()
    robot.set(X_t_1[0], X_t_1[1], X_t_1[2])
    robot.set_noise(5, 0.1, 5)
    robot.straight_line(results, True, True, True)



