"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(last):
    if last == 1:
        return 1
    else:
        return last**2 + sum_of_squares(last-1)


def square_of_sum(last):
    for i in range(1, last):
        last += i
    return last**2


def sos_diff(last):
    return abs(square_of_sum(last)-sum_of_squares(last))


if __name__ == "__main__":
    print(sos_diff(100))
