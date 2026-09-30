#Pgm on numbers
from pack1.subpack1.basicFunc import findMax, isEven, operateOnNum, generate_invoice

isEvenNum = int(input("Enter the number:"))
print(f"{isEvenNum} even is {isEven(isEvenNum)}")

# 2. Get a single line of input separated by spaces
user_string = input("Enter multiple numbers separated by spaces: ").split()
print(f"Maximum of number is {findMax(*user_string)}")

number = int(input("Enter the number:"))
operator = input("Enter the operator as square/cube:")
value = operateOnNum(number,operator)
print(f"value={value}")

try:
    purchasedItems = {}
    totalItems = int(input("Enter the number of items:"))
    for i in range(totalItems):
        key = input("Enter the item name:")
        value = float(input("Enter the price:"))
        purchasedItems[key] = value
    generate_invoice(**purchasedItems)
except Exception as err:
    print(f"Error occurs:{err}")