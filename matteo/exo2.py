h = 15
m = 59

print("Ancienne heure", h,m)
m = m + 1
if m == 60:
    m = 0
    h = h + 1 
print("nouvelle heure", h,m)