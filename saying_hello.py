import turtle
s = turtle.Turtle()
s.shape('turtle')

your_name = input("What's your name?")

s.penup()
s.forward(20)
s.color("blue")
s.write("Hello, " + your_name + "!")
s.backward(20)
