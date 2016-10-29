
def isautomorphic(n):
    l = len(str(n))
    k = n ** 2
    t = k % (10 ** l)
    return t == n
for x in range(10000):
    if isautomorphic(x):
       print(x)

