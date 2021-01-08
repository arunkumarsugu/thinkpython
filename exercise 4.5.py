from swampy.TurtleWorld import Turtle,TurtleWorld
from swampy.World import wait_for_user


World = TurtleWorld()
bob = Turtle()

def arc(t, radius , angle ):
    angle = 360
    n = angle // radius
    for i in range (n):
        t.fd(radius)
        t.lt(radius)


arc(bob, 15, 360)

print(arc)

wait_for_user()
