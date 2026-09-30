#Basic functions used with functional arbitary arguments and kwargs

def taxCalculator(sex,salary):#Tax calculation for an employee
    if sex == 'M':#In case the employee is Male
        if salary > 400000 and salary <= 800000:
            tax = 0.05
        elif salary > 800000 and salary <= 1200000:
            tax = 0.1
        elif salary > 1200000 and salary <= 1600000:
            tax = 0.15
        elif salary > 1600000 and salary <= 2000000:
            tax = 0.20
        elif salary > 20000000 and salary <= 2400000:
            tax = 0.25
        else:
            tax = 0.30
    elif sex == 'F':
        if salary > 1200000 and salary <= 1600000:
            tax = 0.05
        elif salary > 1600000 and salary <= 2000000:
            tax = 0.1
        elif salary > 20000000 and salary <= 2400000:
            tax = 0.15
        elif salary >=2400000:
            tax = 0.20
        else:
            tax=0
    return tax

#Used for calculating the bonus based on the rating of the employee performance
def bonusCalculator(perfLevel):
    if perfLevel == 'H':
        bonus = 0.3
    elif perfLevel == 'M':
        bonus = 0.2
    else:
        bonus = 0.1
    return bonus

#Used for calculating the pf based on the employee salary
def pfCalculator(salary):
    if salary > 400000 and salary <= 800000:
        pf = 0.3
    elif salary > 800000 and salary <= 2500000:
        pf = 0.2
    elif salary > 2500000:
        pf = 0.1
    else:
        pf = 0
    return pf

#Find the given number is even and return the result as boolean
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

#Function to find the max of numbers in 2 ways
def findMax(*nums):
    #Below 2 line of code is using the built in function max()
    '''numbers = [float(x) for x in nums]
    return max(numbers)'''
    #Below lines of code does the finding of max numbers without using built in func
    maxNUm = nums[0]
    for num in nums:
        if int(num) > int(maxNUm):
            maxNUm = num
        else:
            maxNUm = maxNUm
    return maxNUm

#Find the square or cube of the given number and return the result
def operateOnNum(num,operator):
    if operator == 'square':
        num = num**2
    elif operator == 'cube':
        num = num**3
    else:
        return 0
    return num

#Generate the invoice for the purchased products
def generate_invoice(**products):
    total = 0
    for k,val in products.items():
        print(f"{k}:Rs.{val}")
        total+=val
    print(f"Total bill value=Rs.{total}")
