#Sample prgs
#prg1:
'''
Use Case 1:
Write a program that asks for an employee’s age.
1. Checks its type is of string (think about using isinstance() function)
2. Converts it to int (continue writing your program from here..)
3. Prints the years pending for retirement, for eg. 60 is the retirement age.
Example:
Enter your age: 40
You will retire in 20 years at Inceptez Technologies.
'''
from sqlite3.dbapi2 import Date

EmpAge=input("Enter Emp Age:")
if(isinstance(EmpAge,str)):
    EmpAge=int(EmpAge)
    print("Emp Age is",EmpAge)
    print("You will retire after",60-EmpAge,"years from",Date.today(),
          "approximately at the year",Date.today().year+(60-EmpAge))

#prg2:
'''
Fix the type error in the following code for salary calculation:

salary = '50000'
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)
'''
salary = '50000'
bonus = 10000
print('Total Salary in Inceptez:Rs.', int(salary) + bonus)

#prg:3
'''
Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
Employee Salary Breakdown
a. Write a program that asks the user for:
employee_name (string)
base_salary (float)
hra_percent (integer)
bonus_amount (float)
B. Convert inputs to the correct datatype if required.
Calculate:
 HRA = base_salary * (hra_percent / 100)
 Total Salary = base_salary + HRA + bonus_amount
C. Print the output like this:
Employee: Arun
Base Salary: 40000.0
HRA @ 20%: 8000.0
Bonus: 5000.0
Total Salary Payable: ₹53000.0
'''
empName=str(input("Enter Emp Name:"))
baseSalary=float(input("Enter Base Salary:"))
hraPercent=int(input("Enter Hra Percent:"))
bonusAmount=float(input("Enter Bonus Amount:"))
HRA = baseSalary * (hraPercent / 100)
TotalSalary = baseSalary + HRA + bonusAmount
print("Employee:",empName)
print("Base Salary:Rs.",baseSalary)
print("Hra Percent@",hraPercent,"%:",HRA)
print("Bonus Amount:",bonusAmount)
print("Total Salary:Rs.",TotalSalary)

#prg:4
'''
Use Case 2: Student Result Classification
a. Write a program that takes marks as input (initially as a string).
B. Check if the value can be converted to float.
C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
Marks >= 90 --> Outstanding
 Marks >= 75 --> Excellent
 Marks >= 50 --> Pass
 Marks < 50 --> Fail
D. If the input is not numeric, print:
 Invalid marks entered — Please provide numeric input.
'''
mark=input("Enter the mark:")
if(isinstance(mark, str) and mark.isnumeric()):
    mark=int(mark)
    if(mark>=90):
        print("Outstanding mark")
    elif(mark>=75):
        print("Excellent mark")
    elif(mark>=50):
        print("Pass")
    elif(mark<50):
        print("Fail")
else:
    print("Invalid mark,kindly provide numeric value,Try again!")


#prg:5
'''
Use Case 3: Bug Fixing — Datatype Mismatch
The below code is intended to calculate total price, but it has datatype errors. Fix it.
Incorrect code:
item_name = input("Enter product name: ")
 price = input("Enter price per item: ")
 quantity = input("Enter quantity: ")
total_cost = price * quantity
print("You purchased " + quantity + " units of " + item_name)
 print("Total payable: " + total_cost)
Expected output after fixing:
Enter product name: Notepad
 Enter price per item: 35.50
 Enter quantity: 3
You purchased 3 units of Notepad
 Total payable: 106.5 INR
'''
item_name = input("Enter product name: ")
price = float(input("Enter price per item: "))
quantity = float(input("Enter quantity: "))
total_cost = price * quantity
print("You purchased " , quantity , " units of " , item_name)
print("Total payable: " , total_cost,"INR")
