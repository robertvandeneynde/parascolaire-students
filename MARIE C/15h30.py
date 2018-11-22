h = 23
m = 59


if m == 59:
    m = m - 59
    h = 0
else:
    m = m + 1
    h = h + 1

print(h ,"h", m)