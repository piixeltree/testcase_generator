
def f(a,b=2):
    if a>1:
        a+=b
    elif b==2:
        a+=3
    else:
        a+=5
    if a<1:
        return 4
    else:
        return 5
