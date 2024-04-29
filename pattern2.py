n=int(input())
for i in range(1,n+1):
    for j in range(n-i+1):
        if j==0 or j==n-i:
          print("*",end=" ")
        else:
           print(" ",end=" ")
    print()  
for i in range(n,0,-1):
    for j in range(n-i+1):
        if j==0 or j==n-i:
          print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

