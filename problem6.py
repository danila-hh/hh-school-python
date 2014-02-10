#http://projecteuler.net/index.php?section=problems&id=6

def sumAndSquare():
        x = 0
        y = 0
        for i in range(1,101):
            x+=i**2
            y+=i
        z=y**2
        return z-x

sumAndSquare();
