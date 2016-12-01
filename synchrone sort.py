def Synchrone(A, B):
     for j in range(len(A) - 1, 0, -1):
        for i in range(0, j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                B[i], B[i + 1] = B[i + 1], B[i]
            elif A[i]==A[i+1]:
                if B[i]>B[i+1]:
                    B[i],B[i+1]=B[i+1],B[i]
A = [4, 2, 2, 2, 2, 2,  5, 1]
B = [2, 4, 123, 1, 33, 2 ,  7,12]
Synchrone(A, B)
print(A)
print(B)
