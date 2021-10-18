even=[]
odd=[]
print("enter the size of the mix list :",end="")
lis=[]
n=int(input())
for i in range(n):
    num=int(input("enter the numbers :"))
    lis.append(num)
for j in lis:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print("list of your entred no. :",lis)
print("list of even no. :",even)
print("list of odd no. :",odd)