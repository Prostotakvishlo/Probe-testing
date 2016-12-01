A=list(map(int,input().split()))
n = 1
s=0
while n < len(A):
     for i in range(len(A)-n):
          if A[i] > A[i+1]:
               A[i],A[i+1] = A[i+1],A[i]
               s+=1
     n += 1
print(s)