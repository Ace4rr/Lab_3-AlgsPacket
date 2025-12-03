def fibo(n: int) -> int:
    if n<0:
        raise ValueError("Negative n")
    a,b=0,1
    for j in range(n):
        a,b=b,a+b
    return a


def fibo_recursive(n: int) -> int:
    if n<0:
        raise ValueError("Negative n")
    if n<=1:
        return n
    return fibo_recursive(n-1)+fibo_recursive(n-2)
