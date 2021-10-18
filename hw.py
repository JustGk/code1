# print("Ans of Q1. :")
# r=input("Enter the radius of circle : ")
# pi=3.14
# A=(int(r).__pow__(2))*pi
# print(f"area of the circle is : {A}")
# #
# #
# print()
# print("Ans of Q2. : ")
# F_name=input('Enter first name : ')
# L_name=input('Enter last name : ')
# print(f"{L_name} {F_name}")
# #
# #
# print()
# print("Ans of Q3. :")
# lst=['red','blue','yellow','black','cyan','magenta']
# print("Given list of colors :",lst)
# print("first and last colors of the list are : ",lst[0::5])
# #lst[start:end:step:]BECAUSE as we have chose step as 5 slicing starts from index 5
#
# print()
# print("Ans of Q4. :")
# num=[33,32,14,56,7,77,88,91,123,132,143,156,456,431,237,66,452,44,46,68,9445,96,233,345]
# print("given list of random numbers : ",num)
#
# evn=[]
# for i in num:
#     if i%2==0:
#         evn.append(i)
#     elif i==237:
#         break
#     else:
#         pass
# print("list of even numbers till 237 number in the sequence : ",evn)
import datetime
class Employee:
        totalEmployee = 0
        males = 0
        females = 0
        def __init__(self,name,designation,gender,doj,salary):
              self.name = name
              self.designation = designation
              self.gender = gender
              self.doj = doj
              self.salary = salary
              Employee.totalEmployee += 1
              if self.gender == 'M':
                      Employee.males += 1
              else:
                      Employee.females += 1

        def totalEmployeeCount(self):
            total=Employee.totalEmployee
            return total
        def genderCount(self):
            print('Males:', Employee.males)
            print('Females:', Employee.females)
        def isSalaryGreater10000(self):
                if self.salary >= 10000:
                    return print(True)
                else:
                    return print(False)

        def isAsstManager(self):
            if self.designation == "Asst Manager":
                print(True)

            else:
                print(False)

        def create(self):
            name = input("Name: ")
            designation = input("Designation: ")
            gender = input("Gender(M/F): ")
            date_entry = input('Enter a date in YYYY-MM-DD format')
            year, month, day = map(int, date_entry.split('-'))
            doj = datetime.date(year, month, day)
            salary = int(input("Salary: "))
            emp=Employee(name,designation,gender,doj,salary)
            return emp

emp_list=[]
def main():
    while (1):
        print("1.Create Employee\n2.Total Employees\n3.Gender count\n4.Employee with salary greater then thousand  \n5.Asst Managers")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            emp_list.append(Employee.create(self=''))
        elif choice == 2:
            print(Employee.totalEmployeeCount(self=''))
        elif choice == 3:
            print(Employee.genderCount(self=''))
        elif choice == 4:
            for emp in emp_list:
                if emp.isSalaryGreater10000():
                    print(emp.name)
        elif choice == 5:
            for emp in emp_list:
                if emp.isAsstManager():
                    print(emp.name)
        else:
            print("Invalid choice")

if __name__=='__main__':
    main()