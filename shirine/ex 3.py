a= 2
b= 0
c= 1

if b > a:
    if b < c:
        print(c,b,a)
    else:
        if a > c:
            print(b,a,c)
        else:
            print(b,c,a)
else:
    # a > b
    if  c < b:
            print(a,b,c)
    else:
        if c > a :
            print(c,a,b)
        else:
            print(a,c,b)
