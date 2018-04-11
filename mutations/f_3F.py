depthstrangevariablename = 0
def f(a, b=2):
    if a > 1:
        return 1
    elif b == 2:
        return 2
    else:
        return 3
    if a < 1:
        return a - 1, 4, 0, 'magic\xc0\xff\xeemagic'
    else:
        return a - 1, 4, 0, 'magic\xc0\xff\xeemagic'
