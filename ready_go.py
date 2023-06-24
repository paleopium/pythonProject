from turtle import Turtle

class ReadyGo(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()

    def getReady(self):
        self.goto(0,0)
        self.write("Ready", align="center", font=("Comic Sans", 72, "normal"))

    def getShoot(self):
        self.goto(0,0)
        self.write("Shoot", align="center", font=("Comic Sans", 72, "normal"))

    def clearWrite(self):
        self.clear()