def isArmstrongNumber(n):
    #True False
    a = []
    t = n
    while t > 0:
        a.append(t % 10)
        t /= 10
    k = len(a)
    s = 0
    for x in a:
        s += x ** k
    return s == n

for x in range(100,10000):
    if isArmstrongNumber(x):print(x)
