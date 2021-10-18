print("for addtion type +\nfor subtraction type -\nfor multiplication type *\nfor divison type /\nfor power of any number type ^\nfor factorial of no. type !")
print("enter which operation do you want to do : ",end="")
op=input()
if op=='+':
    num1=int(input("enter number 1 : "))
    num2=int(input("enter number 2 : "))
    print(int(num2+num1))
elif op=='-':
    num1 = int(input("enter number 1 : "))
    num2 = int(input("enter number 2 : "))
    print(int(num2 - num1))
elif op=='*':
    num1 = int(input("enter number 1 : "))
    num2 = int(input("enter number 2 : "))
    print(int(num2 * num1))
elif op=='/':
    num1 = int(input("enter number 1 : "))
    num2 = int(input("enter number 2 : "))
    print(num2 / num1)
elif op=='^':
    num1=int(input("enter a number : "))
    num2=int(input("enter the power of the number which you want to calcultar : "))
    power=int(num1).__pow__(num2)
    print(power)
elif op=='!':
    num1=int(input("enter a number"))
    if num1==0:
        print("factorial of given numbwer is ", 1)
    else:
        fac=0
        n=num1
        for i in range(num1):
            fac=num1+(num1*(num1+n))
            n-=1
        print("factorial of given numbwer is ",fac)
else:
    pass
