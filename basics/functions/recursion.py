def tryRecursion(n):
    if(n > 0):
        result = n+tryRecursion(n-1)
        print(result)
    else:
        result = 0
    return result

tryRecursion(5)