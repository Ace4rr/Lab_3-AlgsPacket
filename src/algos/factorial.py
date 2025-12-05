def factorial(n: int) -> int:
    """
        Факториал числа

        Args:
            int

        Returns:
            int
        """
    if n<0:
        raise ValueError("Negative n")
    
    rs=1
    for i in range(2,n + 1):
        rs*=i
    return rs

def factorial_recursive(n: int) -> int:
    """
        Факториал числа (через рекурсию)

        Args:
            int

        Returns:
            int
        """
    if n<0:
        raise ValueError("Negative n")
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)
