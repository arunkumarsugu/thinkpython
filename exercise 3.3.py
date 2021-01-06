def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_horizontal():
    print("+ - - - -", end=" ")


def print_vertical():
    print("|        ", end=" ")


def print_horizontals():
    do_four(print_horizontal)
    print("+")


def print_verticals():
    do_four(print_vertical)
    print("|")


def grid():
    print_horizontals()
    do_twice(print_verticals)


def full_grid():
    do_four(grid)
    print_horizontals()



print (full_grid())