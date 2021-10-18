
n=1

lst=[]
# print(len(lst))
from termcolor import colored
from time import sleep
def type_writr(text,*args):
    for ch in text:
        print(ch,end="")
        sleep(0.1)
    return percentage
c=['whiite','yellow','magenta','red','blue','cyan']
t_marks=[]
for i in range(5):
    for i in range(5):
        cc =c[n]
    print(colored(f"Enter The Mark of Subject {n} : ",cc,attrs=['bold','reverse']),end='')
    enter=int(input())
    print(colored(f"{enter}",attrs=['reverse']))
    print()
    passs=enter
    if passs<40:
        print(colored(f"student is failed in subject {n}",'cyan',attrs=['bold']))
        print(colored(f"As student has scored less than 40 marks in subject {n}  he  is failed ",'white',attrs=['bold']))
        lst.append(n)
    n+=1
    t_marks.append(enter)
total_marks=sum(t_marks)
percentage=total_marks*(100/500)
print()
print(colored(type_writr(colored("percentage of the student is :",'yellow',attrs=['bold','reverse']),percentage),'blue',attrs=['bold','reverse']))
def perce(pecentage):
    if percentage >= 75:
        (type_writr(colored("student is passed with distinction ",attrs=['bold','reverse']))),print()
    elif percentage >= 60 and percentage < 75:
        (type_writr(colored("student is passed with 1st class ",attrs=['bold','reverse']))),print()
    elif percentage >= 50 and percentage < 60:
        (type_writr(colored("student is passed with 2nd class ",attrs=['bold','reverse']))),print()
    elif percentage >= 40 and percentage < 50:
        (type_writr(colored("student is passed with 3rd class ",attrs=['bold','reverse']))),print()
    else:
        (type_writr(colored("student is failded",attrs=['bold','reverse']))),print()
percentage=total_marks*(100/500)
perce(percentage)

"\n"
"\n"
"\n"
sub=0
if len(lst)==0:
    print()
else:
    print(colored("students is failed in the following subject : ", 'blue', attrs=['reverse']), end=" ")
for j in range(len(lst)):
      n1=lst[sub]
      c1 = ['whiite', 'yellow', 'magenta', 'red','blue','cyan']
      for i in range(len(lst)):
          cc1 = c1[sub + 1]
      print(colored(n1, cc1, attrs=['bold', 'reverse']), end=" ")
      sub += 1



# if percentage>=75:
#     print(type_writr("student is passed with distinction "))
# elif percentage>=60 and percentage<75:
#     print(type_writr("student is passed with 1st class "))
# elif percentage>=50 and percentage<60:
#     print(type_writr("student is passed with 2nd class "))
# elif percentage>=40 and percentage<50:
#     print(type_writr("student is passed with 3rd class "))
# else:
#     print(type_writr("student is failded"))