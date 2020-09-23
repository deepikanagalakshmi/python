import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(1)

# square
def square():
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
 
#if else
elephant_weight = 3000
ant_weight = 0.1

if elephant_weight > ant_weight:
  square()
else:
  my_turtle.forward(200)
 
#while
pusp_ups = 10
while pusp_ups >= 0:
    my_turtle.forward(10)
    pusp_ups = pusp_ups-1
    


    

