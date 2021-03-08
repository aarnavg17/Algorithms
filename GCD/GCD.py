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
    return b
