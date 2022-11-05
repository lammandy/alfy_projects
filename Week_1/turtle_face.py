import turtle


def rectangle(edge=100):
    for x in range(4):
     t.forward(edge)
     t.right(90)

def ear():
    t.circle(20)
    t.circle(30)

def eye():
    t.circle(10)

def nose():
    for x in range(3):
        t.forward(10)
        t.right(120)

t = turtle.Turtle()

rectangle()
ear()
t.forward(100)
ear()
t.up()
t.backward(33)
t.right(90)
t.forward(33)
t.down()
eye()
t.up()
t.right(90)
t.forward(33)
t.right(90)
t.down()
eye()
t.up()
t.forward(15)
t.right(180)
t.forward(40)
t.down()
t.circle(radius=20, extent=180)
t.up()
t.right(270)
t.forward(15)
t.down()
nose()

