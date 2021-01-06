def do_twice(func, argument):
    func(argument)
    func(argument)


def print_twice(argument):
    print(argument)
    print(argument)


do_twice(print_twice, 'spam')
print(' ')


def do_four(func, argument):
    do_twice(func, argument)
    do_twice(func, argument)


do_four(print_twice, 'spam')
print(' ')