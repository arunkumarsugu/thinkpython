from swampy.TurtleWorld import TurtleWorld,Turtle
from swampy.World import wait_for_user


def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    theta = 0.0
    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.lt(dtheta)
        theta += dtheta


world = TurtleWorld()
bob = Turtle()
bob.delay = 0
draw_spiral(bob, n=1000)

wait_for_user()