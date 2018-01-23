a=1
b=1
c=0
if c<a and c<b :
    print(c)
    if a<b and a>c:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
if a<b and a<c :
    print(a)
    if c<b and c>a:
        print(c)
        print(b)
    else:
        print(b)
        print(c)
if b<a and b<c :
    print(b)
    if c<a and a>b:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
