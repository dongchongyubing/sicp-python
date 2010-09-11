# http://stackoverflow.com/questions/265392/why-is-lazy-evaluation-useful

def inc(x): return x + 1

def dec(x): return x - 1

def add(a, b):
    return b if a == 0 else add(dec(a), inc(b))

def add2(a, b):
    return b if a == 0 else inc(add2(dec(a), b))

################################################################################

import sys

class TailRecurseException:
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(g):
  """
  This function decorates a function with tail call
  optimization. It does this by throwing an exception
  if it is it's own grandparent, and catching such
  exceptions to fake the tail call optimization.

  This function fails if the decorated
  function recurses in a non-tail context.
  """
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException, e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


# max 990
def factorial2(n):
    def fact_iter(product, counter):
        if counter > n:
            return product
        else:
            return fact_iter(counter * product, counter + 1)

    return fact_iter(1, 1)


@tail_call_optimized
def factorial3(n, acc=1):
    return acc if n == 0 else factorial3(n-1, n*acc)


# Ackermann's function: grows super-super fast
def A(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return A(x - 1, A(x, y - 1 ))

