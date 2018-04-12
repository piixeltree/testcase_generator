depthstrangevariablename = 0
def loop_test(a, b):
    i = 0
    while i < a:
        i += 1
        if i > b:
            return i - b, 2, 0, 'magic\xc0\xff\xeemagic'
        else:
            return i - b, 2, 0, 'magic\xc0\xff\xeemagic'
