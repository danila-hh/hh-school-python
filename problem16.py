# http://projecteuler.net/index.php?section=problems&id=16

def bigString():
    x=0
    bigString = str(2**1000)
    for i in bigString:
            x+=int(i)
    return x

bigString();