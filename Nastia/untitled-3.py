# nastiavdb@GMAIL.COM 
a = 3
b = 1
c = 2


if a < c < b :
 print (a,c,b)
elif b < c < a :
 print (b,c,a)
elif c < b < a : 
 print (c,b,a)
elif a < b < c : 
 print (a,b,c) 
elif b < a < c : 
 print (b,a,c) 
elif c < a < b : 
 print (c,a,b)
 
if a < b  :
 if c < b :
  if c > a :
   print (a,c,b)
  else :
   print (c,a,b)
 else :
  print (a,b,c)
else :
 print ()



