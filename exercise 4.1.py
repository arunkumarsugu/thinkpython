from swampy.TurtleWorld import Turtle,TurtleWorld

World = TurtleWorld()
bob = Turtle()
def square(t):
    for i in range (4):
        t.fd(100)
        t.lt(90)


square(bob)