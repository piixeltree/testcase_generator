depthstrangevariablename = 3
def many_variable(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    if a < b:
        if b < c:
            if c < d:
                if d < e:
                    return d - e, 1, 3, 'magic\xc0\xff\xeemagic'
                else:
                    return d - e, 1, 3, 'magic\xc0\xff\xeemagic'
            else:
                return c - d, 1, 2, 'magic\xc0\xff\xeemagic'
        else:
            return b - c, 1, 1, 'magic\xc0\xff\xeemagic'
    else:
        return a - b, 1, 0, 'magic\xc0\xff\xeemagic'


def many_variable(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    if a < b:
        if b < c:
            if c < d:
                if d < e:
                    return d - e, 1, 3, 'magic\xc0\xff\xeemagic'
                else:
                    return d - e, 1, 3, 'magic\xc0\xff\xeemagic'
            else:
                return c - d, 1, 2, 'magic\xc0\xff\xeemagic'
        else:
            return b - c, 1, 1, 'magic\xc0\xff\xeemagic'
    else:
        return a - b, 1, 0, 'magic\xc0\xff\xeemagic'
