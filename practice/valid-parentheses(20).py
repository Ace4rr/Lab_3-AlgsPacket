class Solution(object):
    def isValid(self, s):
        skob=dict(('[]','()','{}'))
        stack=[]
        for idx in s:
            if idx in '{[(':
                stack.append(idx)
            elif len(stack) == 0 or idx != skob[stack.pop()]:
                return False 
        return len(stack) == 0