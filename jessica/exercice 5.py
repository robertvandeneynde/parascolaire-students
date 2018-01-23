
# exercice 5


l = [ 32, 102 , 156 , 46, 56 ]

m = l[0]

print (l)

i = 1
while i < len(l):
   if m <= l[i]:
      m = l[i]

   i = i + 1
    
print (m)