class Solution(object):
    def guessNumber(self, n):
        left, right=1,n
        while left<=right:
            m=(left+right)//2
            result=guess(m)
            if result==0:
                return m
            elif result==-1:
                right=m-1
            else:
                left=m+1