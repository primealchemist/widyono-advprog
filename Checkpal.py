def main():
    x=0
    for i in range(100,999):
        for a in range(100,999):
            x=i*a
            print x
            if chackpal(x):
                print "This is a palendromee."
def chackpal(x):
    pal=str(x)
    revpal=pal[::-1]
    if pal==revpal:
        return True
