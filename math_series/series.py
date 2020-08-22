def fibonacci(n):
    '''
    function that require value then it keep recal with -1 until it is equal 1 and thats called the 'Recursion':
        input ---> value
        output >> represnt the fibonacci series for the input number
    '''
    if n <= 1:
        if n == 0:
            return 0
        else:
            return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    '''
    function that require value then it keep recal with -1 until it is equal 2 and thats called the 'Recursion':
        input ---> value
        output >> represnt the lucas series for the input number
    '''
    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(n,f=0,s=1):
    '''
    function will cheack if your inputs are ether 'fibonacci' or 'lucas' or it will be sum of both..
    '''
    if f == 2 and s == 1:
        return lucas(n)
    elif f == 0 and s == 1:
        return fibonacci(n)
    else:
        return fibonacci(n) + lucas(f)
    