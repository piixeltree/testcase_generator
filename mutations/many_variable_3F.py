depthstrangevariablename = 2
def many_variable(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    if a < b:
        if b < c:
            if c < d:
                return c - d, 4, 2, 'magic\xc0\xff\xeemagic'
            else:
                return c - d, 4, 2, 'magic\xc0\xff\xeemagic'
        else:
            return b - c, 1, 1, 'magic\xc0\xff\xeemagic'
    else:
        return a - b, 1, 0, 'magic\xc0\xff\xeemagic'


def many_variable(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    if a < b:
        if b < c:
            if c < d:
                return c - d, 4, 2, 'magic\xc0\xff\xeemagic'
            else:
                return c - d, 4, 2, 'magic\xc0\xff\xeemagic'
        else:
            return b - c, 1, 1, 'magic\xc0\xff\xeemagic'
    else:
        return a - b, 1, 0, 'magic\xc0\xff\xeemagic'
