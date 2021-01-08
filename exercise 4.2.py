from swampy.TurtleWorld import Turtle,TurtleWorld
from swampy.World import wait_for_user


World = TurtleWorld()
bob = Turtle()
def square(t,length):
    for i in range (4):
        t.fd(length)
        t.lt(length)


square(bob,90)


wait_for_user()
