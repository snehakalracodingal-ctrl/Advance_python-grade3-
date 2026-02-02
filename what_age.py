import turtle
s = turtle.Turtle()
s.shape('turtle')
s.penup()

try:
    age = int(input("How old are you? (Use numbers)"))
    if age >= 10 and age <= 15:
        s.write("You're between 10 and 15 years old")
        s.backward(20)
    elif age < 10:
        s.write("You're less than 10 years old")
        s.backward(20)
    elif age > 15:
        s.write("You're over 15 years old")
except:
    s.backward(100)
    s.write("I don't think I understand that age. Are you using numbers?")
    s.backward(20)
