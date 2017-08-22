#problem 4
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    n = b
    for i in range(x+1):
        while b <= x:
            b *= n
            i += 1
        return i


#problem 5
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    a = len(s1)
    b = len(s2)
    if a == 0 or b == 0:
        return s1 + s2
    else:
        s = ''
        if a >= b:
            for i in range(b):
                s += s1[i] + s2[i]
                i += 1
            return s + s1[b:]
        if a < b:
            for i in range(a):
                s += s1[i] + s2[i]
                i += 1
            return s + s2[a:]


#problem 6
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')


#problem 7
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    for a in range(n / 6 + 1):
        for b in range(n / 9 + 1):
            for c in range(n / 20 + 1):
                if n == 6 * a + 9 * b + 20 * c:
                    return True
                    break
    return False


#problem 8-1
def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float

    returns the best guess when that guess is less than epsilon
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess


#problem 8-2
def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)


#problem 8-3
def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)