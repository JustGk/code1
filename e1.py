basic_pay=float(input("enter employes basic pay :\tRS."))
HRA=print("HRA is: Rs.",((10/100)*(basic_pay)))
TA=print("TA is: Rs.",((5/100)*(basic_pay)))
GSE=print("Gross salary of employee: Rs.",float(basic_pay+(10/100)*(basic_pay)+(5/100)*(basic_pay)))
tax=print("proffestional tax employe should pay:Rs.",float((2/100)*(basic_pay)))
print("Net salary of the employee:Rs.",int(basic_pay+(10/100)*(basic_pay)+(5/100)*(basic_pay))-(2/100)*(basic_pay))
