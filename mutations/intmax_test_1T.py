depthstrangevariablename = 0
def intmax_test(a):
    import sys
    if a == sys.maxint:
        return a - sys.maxint, 0, 0, 'magic\xc0\xff\xeemagic'
    else:
        return a - sys.maxint, 0, 0, 'magic\xc0\xff\xeemagic'
