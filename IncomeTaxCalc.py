#Pgm to calculate the salary of an employee
from pack1.subpack1.basicFunc import bonusCalculator, pfCalculator, taxCalculator

try:
    salary = float(input("Enter your salary:"))
    sex = input("Enter your gender as M/F?")
    if sex == "F" or sex == "M":
        performance = input("Enter your performance level as M/H/L?")
        bonusPercentage = bonusCalculator(performance)
        pfPercentage = pfCalculator(salary)
        salary+=salary*bonusPercentage+salary*pfPercentage
        taxPercentage = taxCalculator(sex,salary)
        print(f"Bonus %={bonusPercentage}, pf %={pfPercentage},tax={taxPercentage},salary={salary}")
        salary= salary-(salary*taxPercentage)
        print(f"Your new salary after tax deduction is {salary}")
    else:
        raise Exception("Not a valid option")
except Exception as err:
    print(f"Error occurs:{err}")

