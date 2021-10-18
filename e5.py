n=str(input("enter  any 3 digit no."))
if len(n)==3:
    i=int(n[0]).__pow__(3)

    d=int(n[1]).__pow__(3)

    h=int(n[2]).__pow__(3)

    sum=str(i+d+h)

    if sum==n:
        print(f"The given no. {n} is a armstrong no.")
    else:
        print(f"The given no. {n} is not a armstrong no.")
elif len(n)<3:
        print("you have enterd a less number  than a 3 digit no.")
else:
    print("you have enterd a greator number  than a 3 digit no.")

