# http://www.kendyck.com/archives/2005/03/20/solution-to-sicp-exercise-17/

def sqrt_iter(guess, prev_guess, x):
    if is_good_enough(guess, prev_guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), guess, x)

def is_good_enough(guess, prev_guess, x):
    return (abs(guess - prev_guess) / guess) < 0.001

def improve(guess, x):
    return average(guess, x/guess)

def average(x, y):
    return (x + y)/2

def square(x):
    return x * x

def sqrt(x):
    return sqrt_iter(1.0, 0.0, x)
