k=int(input())
t1=0
t2=1
nt=0

for i in range(0,k):
    if i==0:
        print(t1,end=",")
        continue
    if i==1:
        print(t2,end=",")
        continue
    nt=t1+t2
    t1=t2
    t2=nt

    print(nt,end=",")
t1=0
t2=1
j=int(input())
print(t1,end=",")
print(t2,end=",")
n=t1+t2

while(n<=j):


    print(n,end=",")
    t1=t2
    t2=n
    n=t1+t2