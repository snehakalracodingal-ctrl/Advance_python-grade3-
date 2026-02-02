import turtle
s = turtle.Turtle()
s.shape('turtle')

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

for each_color in colors:
    angle = 360 / len(colors)
    s.color(each_color)
    s.circle(40)
    s.right(angle)
    s.forward(30)
