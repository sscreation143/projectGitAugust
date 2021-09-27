import turtle

t=turtle.Turtle()
def square():
   
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)

for i in range(200):
    square()
    t.right(10)
