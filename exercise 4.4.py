from swampy.TurtleWorld import Turtle,TurtleWorld
from swampy.World import wait_for_user


World = TurtleWorld()
bob = Turtle()

def circle(t, length , r ):
    n = 360 // r
    for i in range (n):
        t.fd(r)
        t.lt(r)


circle(bob, 10, 20)

print(circle)

wait_for_user()
