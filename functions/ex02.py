"""A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function
that takes a function object as an argument and calls it twice:
def do_twice(f):
    f()
    f()
Here’s an example that uses do_twice to call a function named print_spam twice.
def print_spam():
    print('spam')
do_twice(print_spam)

1. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing
the value as an argument.
2. Copy the definition of print_sum from earlier chapter to your script.
3. Use the modified version of do_twice to call print_twice twice, passing 2 as an argument.
4. Define a new function called do_four that takes a function object and a value and calls the function four times,
passing the value as a parameter. There should be only two statements in the body of this function, not four."""

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""


def do_twice(func, arg):
    """Runs a function twice.

    func: function object
    type func: function
    arg: argument passed to the function
    """
    func(arg)
    func(arg)


def print_square(x):
    """Prints the argument twice.

    arg: any number
    """
    print(x ** 2)
    print(x ** 2)


def do_four(func, arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)


def main():
    do_twice(print_square, 2)
    print('')

    do_four(print_square, 2)


if __name__ == '__main__':
    main()
