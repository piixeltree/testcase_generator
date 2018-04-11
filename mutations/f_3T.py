depthstrangevariablename = 0
def f(a, b=2):
    if a > 1:
        a += b
    elif b == 2:
        a += 3
    else:
        a += 5
    if a < 1:
        return a - 1, 1, 0, 'magic\xc0\xff\xeemagic'
    else:
        return a - 1, 1, 0, 'magic\xc0\xff\xeemagic'
