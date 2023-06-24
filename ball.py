from turtle import Turtle
import math

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(4, 4)
        self.penup()
        self.color("OrangeRed1")
        self.movingSpeed = 6
        self.goto(-420, -260)
        self.power = 2.9
        self.x_direction = 1
        self.angle = 45
        self.velocity = 20
        self.resetGameBall()

    def move(self):
        # Define gravitational constant and vertical acceleration
        g = 9.8  # m/s^2
        ay = -0.5  # m/s^2

        # Define time interval
        dt = 0.5


        # Update position
        x = self.xcor() + self.vx * dt * self.x_direction *(self.power/2)
        y = self.ycor() + self.vy * dt * self.power + 0.5 * ay * dt**2
        self.goto(x, y)

        # Update velocity
        self.vy += ay * dt


    def wallbounce(self):
        self.x_direction *= -1

    def resetGameBall(self):
        self.velocity=20
        self.x_direction=1
        theta = math.radians(self.angle)

        self.vx = self.velocity * math.cos(theta)
        self.vy = self.velocity * math.sin(theta)
        self.goto(-420, -260)
