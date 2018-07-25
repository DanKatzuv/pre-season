"""
The built-in function eval takes a string and evaluates it using the Python interpreter. For example:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it
evaluated
"""


def eval_loop():
    """
    Prompt the user, take the resulting input and evaluate it using eval and print the result, until 'done' is entered.
    :return: None
    """
    while True:
        inputted = input('Enter an expression: ')
        if inputted == 'done':
            break
        eval(inputted)


def main():
    eval_loop()


if __name__ == '__main__':
    main()
