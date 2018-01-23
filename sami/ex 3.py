a = 2
b = 6
c = 1

if a < b:
    if a < c:
        if b > c:
            print(a,c,b)
        else:
            print(a,b,c)
    else:
        print(c,a,b)
else:
    # veut dire a>=b
    if c < b:
        
        