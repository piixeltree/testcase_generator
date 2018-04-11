
def asdf(a):
    if a==0:
        return 2
    return 3


def abs(a):
    if a>0:
        return a
    else:
        return -1*a

def sum(a,b):
    return a+b

def sum_a_to_b(a,b):
    sumi = 0
    i = a
    while i<=b:
        sumi+=i
        i+=1
    return sumi
