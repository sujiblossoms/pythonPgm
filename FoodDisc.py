#Pgm to find the food discount
continueRun='y'
minCartValue,maxDis=600,100
def foodDis(cart):
    if (cart >= minCartValue):
        dis = (cart * 10) / 100
        if (dis > maxDis):
            print("Max discount reached,so giving flat discount")
            finalPrice = cart - maxDis
        else:
            finalPrice = cart - dis
        print("The final price after discount:Rs.", finalPrice)
    else:
        print("kindly purchase items for another Rs.", (minCartValue - cart), "to meet the cart value")

while(continueRun=='y'):
    try:
        cart=float(input("Enter the cart value:"))
        foodDis(cart)
        continueRun = input("Do you want to continue?(y/n)")
    except Exception as err:
        print(f"Error occurs:{err}")

