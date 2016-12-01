L=True
s=0
while L==True:
    A=input().split()
    if int(A[0])==int(A[1])==0:
        break
    else:
        N1=int(A[0])
        N2=int(A[1])
        if N1%2==0 and N2%7==0 and (len(str(N1))>=3 or len(str(N2))):
            s+=1
print(s)