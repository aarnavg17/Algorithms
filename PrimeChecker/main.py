def primecheck(n):
    num_list = [False, True] * (n // 2)
    num_list[1] = False
    for num in range(3, n, 2):
        if num_list[num]:
            for i in range(num ** 2, n, num * 2):
                num_list[i] = False
    for x in range(3, len(num_list), 2):
        if num_list[x]:
            if not (n % x):
                return False
    return True
