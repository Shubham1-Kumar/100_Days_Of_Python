import random
import turtle

from Python_Practice.Grade import score
tim  = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
tim.pensize(10)
color_list = ["firebrick","brown","medium violet red","hot pink","deep pink","yellow","magenta","rosy brown","medium spring green","dark slate gray","blue"]
directions = [0,90,180,270]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r,g,b)
    return color_tuple

i = 200
tim.speed(0)
while i:
    tim.color(random_color())
    if random.choice(directions) == 90:
        tim.back(30)
    tim.seth(random.choice(directions))
    tim.forward(30)
    i-=1