a=12 
b=45
c=645

if a<b<c:
    print(a,b,c)
    
else:
    if b<c<a:
        print(b,c,a)
    else:
        if c<a<b:
            print(c,a,b)
        else:
            if a<c<b:
                print(a,c,b)
                
            else:
                if c<a<b:
                    print(c,a,b)
                else:
                    if b<a<c:
                        print(b,a,c)
                    