def prime_factors (n):
    result = []
    x = 2
    while n != 1:
        if n%x == 0:
            n = n//x
            result.append(x)
        else:
            x += 1
    return result
