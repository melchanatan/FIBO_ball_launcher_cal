import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.lines as lines
import numpy as np
import math


class FieldSetup:

    def __init__(self, tall_wall=False):
        self.starting_length = 0.8
        self.starting_to_wall = 1
        self.wall_to_target = 1
        self.target_max_width = .5
        self.wall_width = .1

        self.wall_height = 1 if tall_wall else 0.5

    def initialize_field(self, crop_graph=True):
        # Set Graph limit
        if crop_graph:
            plt.xlim(0, self.starting_length + self.starting_to_wall + self.wall_to_target + self.target_max_width)
            plt.ylim(-0.1, self.wall_height+0.5)
        plt.axhline(0)

        # Draw Starting Zone
        plt.hlines(0, xmin=0, xmax=self.starting_length, lw=3, colors="g")
        plt.text(-0.01, -0.05, "starting zone")

        # Draw Wall
        zero_to_wall = self.starting_length + self.starting_to_wall
        plt.vlines(zero_to_wall-(self.wall_width/2), ymin=0, ymax=self.wall_height)
        plt.hlines(self.wall_height, xmin=zero_to_wall-(self.wall_width/2), xmax=zero_to_wall+(self.wall_width/2))
        plt.vlines(zero_to_wall+(self.wall_width / 2), ymin=0, ymax=self.wall_height)

        # Draw target
        zero_to_target = self.starting_length+self.starting_to_wall+self.wall_to_target
        plt.hlines(0, zero_to_target, zero_to_target+self.target_max_width, lw=3, colors="r")


class Ball:

    def __init__(self):
        self.height = 0.5
        self.theta_degree = math.radians(45)
        # self.initial_velocity = 4.6
        self.gravity = 9.8

    def calculate_initial_velocity(self, wall_height):
        calculated_initial_velocity = (math.sqrt(2*self.gravity*wall_height))/math.sin(self.theta_degree)
        return calculated_initial_velocity

    def generate_movement(self, u, theta_degree, robot_position):
        theta_degree = math.radians(theta_degree)
        xs = []
        ys = []
        for x in range(0, 350):
            x = x / 100
            y = (x * math.tan(theta_degree) - ((self.gravity * x ** 2) / (2 * u ** 2 * math.cos(theta_degree) ** 2)))
            xs.append(x+robot_position)
            ys.append(y)
        return [xs, ys]


ball = Ball()
starting_initial_velocity = ball.calculate_initial_velocity(0.5)
starting_degree = 45
movement_points = ball.generate_movement(starting_initial_velocity, starting_degree, 0.8)
fig = plt.figure()
ax = fig.subplots()
p, = plt.plot(movement_points[0], movement_points[1])

# generate_field()
fieldSetup = FieldSetup(tall_wall=True)
fieldSetup.initialize_field(crop_graph=True)

plt.subplots_adjust(bottom=0.35)

axes_degree = plt.axes([0.25, 0.2, 0.65, 0.03])
axes_initial_velocity = plt.axes([0.25, 0.15, 0.65, 0.03])
axes_robot_position = plt.axes([0.25, 0.10, 0.65, 0.03])
degree = Slider(axes_degree, 'Degree', 0.0, 90, starting_degree)
initial_velocity = Slider(axes_initial_velocity, 'Initial Velocity', 1, starting_initial_velocity+10, starting_initial_velocity)
robot_position = Slider(axes_robot_position, 'Position', 0.0, 0.8, 0.8)

def update_initial_variable(val):
    d = degree.val
    u = initial_velocity.val
    rp = robot_position.val
    m = ball.generate_movement(theta_degree=d, u=u, robot_position=rp)
    p.set_ydata(m[1])
    p.set_xdata(m[0])
    fig.canvas.draw()


# Call update function when slider value is changed
degree.on_changed(update_initial_variable)
initial_velocity.on_changed(update_initial_variable)

plt.show()