'''n=int(input())
for i in range(2,n):
 if(n%i==0):
    print(" not prime")
    break
else:
    print("prime no")'''

n=int(input())
def prime(n)->bool:
   
 for i in range(2,n):
  if(n%i==0):
    flag=0
    return 0
 else:
  flag=1
  return 1
 flag=prime(n)
 if (flag==0):
    print(" not prime")

 else:
    print("prime no")
    