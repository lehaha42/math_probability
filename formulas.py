from math import sqrt, e, pi


def C(a, b):
    return fact(b)/(fact(a)*fact(b-a))


def A(a, b):
    return fact(b)/fact(b-a)


def P(a, b, c):
    return C(a, b) * c**a * (1-c)**(b-a)


def P2(k, n, p):
    s = sqrt(n * p * (1 - p))
    x = (k - n * p) / s
    return phi(x) / s


def phi(x):
    a = e**(-(x * x / 2))
    return a / sqrt(2 * pi)


def fact(n):
    if n<2:
        return 1
    out = 1
    for i in range(2, n+1):
        out *= i
    return out
