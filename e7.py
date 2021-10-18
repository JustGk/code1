n=int(input("enter a number: "))
print(n**.5)
print(n*n)
print(n.__pow__(3))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")

            break

        elif n%i!=0:
            print(n,"is a prime number")
            break
else:
    print("given number is not a prime no.")
N=int(input("Enter a number : "))
a=1
ls=[]

while N%2==0:
    ls.append(2)
    print(2,'|',int(N))
    N=N/2

for i in range(3,int(N)):
    if N%i==0:
        print(int(i),'|',int(N))
        ls.append(i)
        N=N/i
        print(int(N),'|',end=" ")
if N>2:
    print(int(N))
    ls.append(int(N))

