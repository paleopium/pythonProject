from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score=0
        with open("highscore.txt","r") as my_file:
            self.highscoreX=int(my_file.read())

        self.updateScore()

    def restart(self):
        self.score=0
        self.updateScore()
    def updateScore(self):
        self.clear()
        self.goto(-400,250)
        self.write(f"Score {self.score}",align="center",font=("Courier",35,"normal"))
        self.goto(-410, 220)
        self.write(f"Highscore {self.highscoreX}", align="center", font=("Courier", 18, "normal"))

    def gameOver(self):
        if self.score>self.highscoreX:
            with open("highscore.txt","w") as my_file:
                my_file.write(f"{self.score}")
        self.goto(0,-50)
        self.write(f"Game Over", align="center", font=("Courier", 80, "normal"))
        self.goto(0, -150)
        self.write("escape-key to leave", align="center", font=("Courier", 24, "normal"))
        self.goto(0, -100)
        self.write("Restart in 10 sec", align="center", font=("Courier", 24, "normal"))

