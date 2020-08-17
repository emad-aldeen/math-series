def fibonacci(n):
    if n <= 1:
        if n == 0:
            return 0
        else:
            return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(n,f=0,s=1):
    if f >= 1 and s >= 2:
        return lucas(n)
    else:
        return fibonacci(n)
    