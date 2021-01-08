from swampy.TurtleWorld import Turtle,TurtleWorld
from swampy.World import wait_for_user


World = TurtleWorld()
bob = Turtle()
def polygon(t,length,n):
    for i in range (n):
        t.fd(length)
        t.lt(45)


polygon(bob,60,8)

print(polygon)

wait_for_user()
