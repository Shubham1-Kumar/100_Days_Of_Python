import turtle
tim = turtle.Turtle()
tim.shape("turtle")
tim.color("blue")
i =0
while i!=5:
 tim.forward(100)
 tim.back(100)
 i+=1

tim.getpen()
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()