def partition(arr):
    p=arr[0]
    left=[]
    equal=[]
    right=[]
    for x in arr:
        if x<p:
            left.append(x)
        elif x>p:
            right.append(x)
        else:
            equal.append(x)
    return left+equal+right

n=int(input())
arr=list(map(int, input().split()))
print(*partition(arr))