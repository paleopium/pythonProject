import random
from turtle import Turtle, Screen
from ball import Ball
from basket import Basket
from scoreboard import Score
import serial
import time
import statistics
from ready_go import ReadyGo

# Establish serial connection
serial_obj = serial.Serial('COM7', 115200)  # Replace 'COM7' with the appropriate port for your system

# Set the duration of data collection (in seconds)
duration = 3

#median 1 and 2



def calculate_the_data():
    # Create an empty list to store the sensor data
    sensor_data = []

    # Get the start time
    start_time = time.time()

    # Read sensor data for the specified duration
    while (time.time() - start_time) < duration:
        if serial_obj.in_waiting > 0:
            # Read data from Arduino
            data = serial_obj.readline().decode().rstrip()

            # Convert data to float (assuming the sensor data is in floating-point format)
            try:
                data = float(data)
            except ValueError:
                continue

            # Append data to the sensor_data list
            sensor_data.append(data)

    return statistics.median(sensor_data)




screen=Screen()
screen.title("Basketball")
screen.bgcolor("black")
screen.setup(1000,600)
screen.tracer(0)
screen.listen()

screen.onkeypress(screen.bye,"Escape")

basket=Basket()
ball=Ball()
scoreboard=Score()
readygo= ReadyGo()
def calculatePower(medi1,medi2):
    if(5.00<=medi1-medi2<=7.00):
        ball.power = random.choice([2.7,2.8,2.9])
    if(7.00<medi1-medi2):
        ball.power = random.randint(3,10)
    if (medi1 - medi2<5.00):
        ball.power = random.choice([2.6,2.3,2,1.7,1.3,1])


ball.velocity=200
game_is_not_over=True
any_live=True
while True:

    while game_is_not_over:
        screen.update()
        while any_live==True:
            readygo.getReady()
            readygo.clear()
            print("Go medi1")
            medi1 = calculate_the_data()
            print(medi1)
            time.sleep(1)
            readygo.getShoot()
            readygo.clear()
            print("Go medi2")
            medi2 = calculate_the_data()
            print(medi2)
            calculatePower(medi1, medi2)
            any_live=False

        time.sleep(0.000001)
        ball.move()

        #make a point
        if 310<ball.xcor()<430 and ball.ycor()>basket.ycor():
            if ball.distance(basket)<30:
                scoreboard.score+=1
                scoreboard.updateScore()
                ball.resetGameBall()
                any_live=True

        #bounce against basket
        if 290<=ball.xcor()<=310 and basket.ycor()-40<=ball.ycor()<=basket.ycor()+40:
            ball.wallbounce()
            #game_is_not_over=False

        #bounce against wall
        if ball.xcor()>basket.xcor()+30 :
            ball.wallbounce()

        #under basket
        if ball.ycor()<-280:
            game_is_not_over=False
            scoreboard.gameOver()

    time.sleep(10)
    scoreboard.restart()
    ball.resetGameBall()
    game_is_not_over=True
    any_live=True



# Close the serial connection


screen.exitonclick()
serial_obj.close()