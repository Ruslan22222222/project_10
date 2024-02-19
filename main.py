
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed(40)
# tim.color(random_color())

for _ in range(1000):
    tim.circle(100)
    tim.color(random_color())
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)
    



screen = t.Screen()
screen.exitonclick()




   



