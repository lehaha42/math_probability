

def C(a, b):
    return fact(b)/(fact(a)*fact(b-a))


def A(a, b):
    return fact(b)/fact(b-a)


def fact(n):
    if n<2:
        return 1
    out = 1
    for i in range(2, n+1):
        out *= i
    return out
