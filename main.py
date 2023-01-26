import matplotlib.pyplot as plt
import numpy as np
import math


class FieldSetup:

    def __init__(self):
        self.starting_length = 0.5
        self.starting_to_wall = 1
        self.wall_to_target = 1
        self.target_max_width = .5
        self.wall_width = .1

        self.wall_height = 0.5

    def initialize_field(self, crop_graph=True):
        # Set Graph limit
        if crop_graph:
            plt.xlim(0, self.starting_length + self.starting_to_wall + self.wall_to_target + self.target_max_width)
            plt.ylim(-0.1, 1)
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
        self.height = 10
        self.theta_degree = 30
        self.initial_velocity = 5
        self.gravity = 9.8

    def calculate_initial_velocity(self, wall_height):
        self.initial_velocity = ((2*self.gravity*wall_height)/math.sin(self.theta_degree)**2)**1/2
        print(self.initial_velocity)

    def generate_movement(self):
        xs = []
        ys = []
        for x in range(-100, 100):
            y = (x*math.tan(self.theta_degree)) - ((self.gravity*x**2)/(2*(self.initial_velocity**2 * math.cos(self.theta_degree)**2)))
            xs.append(x)
            ys.append(y)
            print(y)
        plt.plot(xs, ys)


fieldSetup = FieldSetup()
fieldSetup.initialize_field(crop_graph=False)

ball = Ball()
ball.calculate_initial_velocity(fieldSetup.wall_height)
ball.generate_movement()

plt.show()