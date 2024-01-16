def mySqrt(x):
    if x == 0 or x == 1:
        return x

    result = 1
    while result * result <= x:
        result += 1

    return result - 1