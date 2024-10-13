import turtle

tom = turtle.Turtle()
screen = turtle.Screen()

angle = 120
length = 100
i =5
while i:
    tom.forward(100)
    tom.right(angle)
    tom.forward(100)
    tom.right(angle)
    tom.forward(100)
    tom.left(120)
    tom.forward(100)
    tom.left(120)
    tom.forward(100)
    i-=1




tom.getscreen()

screen.exitonclick()

