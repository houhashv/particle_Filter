# particle_Filter
this is a partical filter implementation in python
Intelligent Robotics Systems
Exercise 2: Particle Filter
Lecturer: Armin Biess, Ph.D.
Due date: 9.5.2019
Monte Carlo Localization of a mobile robot using landmarks [100 pts]
Consider a planar robot with three DOFs x = (x, y, θ) operating in a world of size 100 × 100. The world
includes four landmarks at
m = {(20, 20),(80, 80),(20, 80),(80, 20)} ,
as shown in the figure
The robot can take two motor commands, a turn movement command u1,(u1 ∈ [0, 2π)) and a forward
movement command u2 (u2 > 0). The deterministic motion model of the robot is given by
θ
0 = θ + u1 ,
x
0 = x + u2 cos θ
0
,
y
0 = y + u2 sin θ
0
,
For the implementation of the MCL algorithm two Matlab classes are provided. The cWorld class defines
the world of the robot and includes a plot function. The cRobot class initializes a robot with an arbitrary
pose in the world. This class includes the following functions:
• set: sets new pose of the robot
• print: prints the pose of the robot to the Matlab prompt
• plot: plots the robot in the world [different colors and different plot styles - ’robot’ and ’particle’
- can be chosen]
• set noise: sets the noise parameters (forward noise, turn noise, sense noise)
a.)[10 pts] Experiment with the cRobot class by plotting three robots into the world with the following
poses (x, y, θ): {(40, 40, 0), (60, 50, π/2), (30, 70, 3π/4)} and by printing these poses to the Matlab prompt.
Initialize the world and robot by typing at the Matlab prompt:
>> myworld = cWorld();
>> myworld.plot;
>> myrobot = cRobot();
b.)[10 pts] Add a function move to your robot class, which takes as input the two motor commands and
outputs the new pose. Assume that the real motor commands are noisy and corrupted with Gaussian noise
of zero means and standard deviations σ1 = 0.1 (rad) (turn noise) and σ2 = 5 (forward noise), respectively.
c.)[10 pts] Add a function sense to your robot class that outputs the distances to the four landmarks.
Assume that the measurements are corrupted by Gaussian noise with zero mean and standard deviation
r = 5 (sensor noise).
d.)[10 pts] Add a function measurement probability to your robot class that takes the measurement from
part c.) as input and outputs the probability for this measurement to be observed when being in pose x.
e.) [5 pts] The robot performs now the following five actions:
1. move by u1 = 0, u2 = 60,
2. move by u1 = π/3, u2 = 30,
3. move by u1 = π/4, u2 = 30,
4. move by u1 = π/4, u2 = 20,
5. move by u1 = π/4, u2 = 40,
starting from pose x = (10, 15, 0) at time t = 0. Plot the robot poses and the robot path (as a dotted line)
resulting from the action commands assuming that the robot follows the action commands exactly, i.e., there
is no noise in the system.
f.)[5 pts] Plot the true robot poses and robot path (as a solid line) into the same figure. The true poses and
the true robot path result from the noisy motor commands (noise: zero means and standard deviations σ1
and σ2) (Make sure to store the true pose because it is needed for the particle filter).
g.)[50 pts] Implement a particle filter with N = 1000 particles to estimate the poses and the path of
the robot by taking measurements of the landmarks. Start by initializing the particles at the initial pose
x = (10, 15, 0) (remember that each particle corresponds to a hypothesis of a possible robot pose). After each
motor command (prediction step) the robot takes a measurement from its true pose and updates its belief
(measurement update). Plot the particles before the measurement update (in black), i.e., before resampling,
and after the measurement update (in gray), i.e., after resampling, using the ’particle’ plot-style of the
plot function in the cRobot class. Determine the estimated poses and estimated path by averaging over
all particles at each time step. Plot the estimated path (as a dash-dotted line) and compare it with the
commanded and true path.
Remarks:
1. It is assumed that the world is cyclic, i.e., if the robot exits on one side it will re-enter on the opposing
side.
2. It is assumed that the problem of correspondences between measurement and number of landmark is
solved, i.e., the i-th measurement corresponds to the i-th landmark.
3. For the implementation of the particle filter, initialize separately N = 1000 instances of the cRobot class
for (1) the initialization step, (2) the prediction step and (3) the measurement update (resampling).
4. Please provide well-documented Matlab code. Your solution should contain two figures - one for part
a.) and one for part e.)-g.).
