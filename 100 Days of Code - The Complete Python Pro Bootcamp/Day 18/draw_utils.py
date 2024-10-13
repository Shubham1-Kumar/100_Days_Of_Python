import random
import turtle
tom = turtle.Turtle()
screen = turtle.Screen()
color_list = ["firebrick","brown","medium violet red","hot pink","deep pink","yellow","magenta","rosy brown","medium spring green","dark slate gray","blue"]
def draw_shape_up(numer_of_sides):
    angle = 360/numer_of_sides
    for _ in range(numer_of_sides):
            tom.forward(100)
            tom.left(angle)
def draw_shape_down(numer_of_sides):
    angle = 360/numer_of_sides
    for _ in range(numer_of_sides):
            tom.forward(100)
            tom.right(angle)
for shape_side_n in range(3,11):
    tom.color(random.choice(color_list))
    draw_shape_down(shape_side_n)
    draw_shape_up(shape_side_n)

def dashed_line():
    lines = 25
    while lines:
        tom.forward(10)
        tom.up()
        tom.forward(10)
        tom.down()
        lines-=1

tom.getscreen()
screen.exitonclick()