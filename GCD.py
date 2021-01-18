import time
start = time.time()

def GCD(a, b):
    if not a > b:
        temp = a
        a = b
        b = temp
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    print (b)

GCD(18, 35)
print(time.time() - start)