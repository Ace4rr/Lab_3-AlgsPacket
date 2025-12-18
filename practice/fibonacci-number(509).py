class Solution(object):
    def fib(self, n):
        f1,f2=0,1
        for gg in range(n):
            f1,f2=f2,f1+f2
        return f1