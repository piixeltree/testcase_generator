depthstrangevariablename = 8
def many_variable(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    if a < b:
        if b < c:
            if c < d:
                if d < e:
                    if e < f:
                        if f < g:
                            if g < h:
                                if h < i:
                                    if i < j:
                                        return (i - j, 4, 8,
                                            'magic\xc0\xff\xeemagic')
                                    else:
                                        return (i - j, 4, 8,
                                            'magic\xc0\xff\xeemagic')
                                else:
                                    return (h - i, 1, 7,
                                        'magic\xc0\xff\xeemagic')
                            else:
                                return g - h, 1, 6, 'magic\xc0\xff\xeemagic'
                        else:
                            return f - g, 1, 5, 'magic\xc0\xff\xeemagic'
                    else:
                        return e - f, 1, 4, 'magic\xc0\xff\xeemagic'
                else:
                    return d - e, 1, 3, 'magic\xc0\xff\xeemagic'
            else:
                return c - d, 1, 2, 'magic\xc0\xff\xeemagic'
        else:
            return b - c, 1, 1, 'magic\xc0\xff\xeemagic'
    else:
        return a - b, 1, 0, 'magic\xc0\xff\xeemagic'
