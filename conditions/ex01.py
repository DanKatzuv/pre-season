"""Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
a^n + b^n = c^n
for any values of n greater than 2.
1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
checks to see if Fermat’s theorem holds. If n is greater than 2 and
a^n + b^n = c^n
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem."""


def check_fermat(a, b, c, n):
    """
    Prints whether Fermat was worng.
    :param a: first base
    :rtype n: int
    :param b: second base
    :rtype b: int
    :param c: third base
    :rtype c: int
    :param n: exponent
    :rtype n: int
    :return: None
    """
    if n > 2 and a ** n + b ** n == c ** n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')


def user_check_fermat():
    """
    Prints whether Fermat was wrong, with user input.
    :return: None
    """
    a = int(input('Enter a: '))
    c = int(input('Enter b: '))
    b = int(input('Enter c: '))
    n = int(input('Enter n: '))
    check_fermat(a, b, c, n)


def main():
    user_check_fermat()


if __name__ == '__main__':
    main()
