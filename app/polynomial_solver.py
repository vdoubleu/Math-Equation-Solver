from parser import *


def evaluate(polynomial, x):
    val = 0
    for exponent in polynomial.keys():
        val += polynomial[exponent]*(x**exponent)
    return val


def differentiate(polynomial):
    deriv = {}
    for exponent in polynomial:
        deriv[exponent-1] = exponent*polynomial[exponent]
    return dict(filter(lambda x: x[0] > -1, deriv.items()))
    

def lower_bound(polynomial):
    test = -10
    while evaluate(polynomial, test) * evaluate(polynomial, test*10) < 0:
        test *= 10
    return test


def upper_bound(polynomial):
    test = 10
    while evaluate(polynomial, test) * evaluate(polynomial, test*10) < 0:
        test *= 10
    return test


def newton(polynomial, lower):
    for i in range(10):
        slope = evaluate(differentiate(polynomial), lower)
        temp = evaluate(polynomial, lower)
        diff = temp / slope
        lower -= diff
    return lower


def find_roots(polynomial, lower, higher):
    roots = set()
    step = 0.01
    i = lower

    while i <= higher:
        if evaluate(polynomial, i) * evaluate(polynomial, i+step) <= 0:
            roots.add(newton(polynomial, i))
        i += step
    return list(roots)


if __name__ == '__main__':

    s = 'x^2-1'
    s = clean_string(s)
    print(s)

    polynomial = parse_exponents(s)
    print(polynomial)

    derivative = differentiate(polynomial)

    print(derivative)

    print('Lower bound:', lower_bound(polynomial))
    print('Upper bound:', upper_bound(polynomial))
    print('Roots:', find_roots(polynomial, lower_bound(polynomial), upper_bound(polynomial)))