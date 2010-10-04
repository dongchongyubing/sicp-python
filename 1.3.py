def cube(x):
    return x*x*x

def sum_integers(a, b):
    return 0 if a > b else a + sum_integers(a + 1, b)

def sum_cubes(a, b):
    return 0 if a > b else cube(a) + sum_cubes(a + 1, b)

def pi_sum(a, b):
    if a > b:
        return 0
    else:
        return (1.0 / (a * (a + 2))) + pi_sum(a + 4, b)

def mysum(term, a, next_term, b):
    if a > b:
        return 0
    else:
        return term(a) + mysum(term, next_term(a), next_term, b)

def inc(n): return n + 1

def sum_cubes2(a, b):
    return mysum(cube, a, inc, b)

def identity(x):
    return x

def sum_integers2(a, b):
    return mysum(identity, a, inc, b)

def pi_sum2(a, b):
    def pi_term(x):
        return 1.0 / (x * (x + 2))

    def pi_next(x):
        return x + 4

    return mysum(pi_term, a, pi_next, b)


def pi_sum3(a, b):
    return mysum(lambda x: 1.0 / (x * (x + 2)), a, lambda x: x + 4, b)


def integral(f, a, b, dx):
    def add_dx(x): return x + dx
    return mysum(f, a + (dx / 2.0), add_dx, b) * dx

def integral2(f, a, b, dx):
    return mysum(f, a + (dx / 2.0), lambda x: x + dx, b) * dx

#integral(cube, 0, 1, 0.01)
# sys.setrecursionlimit(2000)
# integral(cube, 0, 1, 0.001)

