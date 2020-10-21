from exturtle_test import *

t = Turtle()


# was only here for half an hour so this was all I had time to do!

def body(t):
    left(t, 44)
    right(t, 36)
    for counter in range(10):
        forward(t, 10)
        left(t, 36)
    right(t, 270)
    right(t, 180)
    forward(t, 50)
    right(t, 90)
    forward(t, 50)
    right(t, 180)
    forward(t, 100)
    right(t, 180)
    forward(t, 50)
    right(t, 270)
    forward(t, 50)
    right(t, 45)
    forward(t, 50)
    right(t, 180)
    forward(t, 50)
    right(t, 90)
    forward(t, 50)


color(t, 'violet')
pensize(t, 5)
print(body(t))

mainloop()
