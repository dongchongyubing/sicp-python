def square(x):
    return x * x

def sum_of_squares(x, y):
    return square(x) + square(y)

def f(a):
    return sum_of_squares(a + 1, a * 2)

######################################################################

def sqrt_iter(guess, x):
    if is_good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def improve(guess, x):
    return average(guess, x/guess)

def average(x, y):
    return (x + y)/2

def is_good_enough(guess, x):
    return abs(square(guess) - x) < 0.001

def sqrt(x):
    return sqrt_iter(1.0, x)

######################################################################

def average(x, y):
    return (x + y)/2

def sqrt2(x):
    def is_good_enough(guess, x):
        return abs(square(guess) - x) < 0.001

    def improve(guess, x):
        return average(guess, x/guess)

    def sqrt_iter(guess, x):
        if is_good_enough(guess, x):
            return guess
        else:
            return sqrt_iter(improve(guess, x), x)

    return sqrt_iter(1.0, x)

# lexical scoping

def sqrt3(x):
    def is_good_enough(guess):
        return abs(square(guess) - x) < 0.001

    def improve(guess):
        return average(guess, x/guess)

    def sqrt_iter(guess):
        if is_good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    return sqrt_iter(1.0)
