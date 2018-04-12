depthstrangevariablename = 0
import sys


def intmax_test(a):
    if a == sys.maxint:
        return a - sys.maxint, 0, 0, 'magic\xc0\xff\xeemagic'
    else:
        return a - sys.maxint, 0, 0, 'magic\xc0\xff\xeemagic'
