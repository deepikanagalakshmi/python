import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(1)

#triangle
def triangle():
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(135)
    my_turtle.forward(142)

for count in range(3):
    triangle()


