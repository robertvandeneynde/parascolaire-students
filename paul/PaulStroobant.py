l = [1, 2, 7, 2, 2, 3]

if l[0] > l[1]:
    m = l[0]
else:
    m = l[1]

n = 2
while n <= 5:
    if l[n] > m:
        m = l[n]
    n = n + 1

# while m > l[n]
#    n = n + 1

print("max =", m)