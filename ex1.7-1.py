def sqrt_iter(guess, x):
    next_guess = improve(guess, x)
    if is_good_enough(guess, next_guess, x):
        return guess
    else:
        return sqrt_iter(next_guess, x)

def is_good_enough(guess, next_guess, x):
    return next_guess / guess > 0.999999

def improve(guess, x):
    return average(guess, x/guess)

def average(x, y):
    return (x + y)/2

def square(x):
    return x * x

def sqrt(x):
    return sqrt_iter(1.0, x)
