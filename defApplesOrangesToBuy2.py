#    This program will ask the user how many apples and oranges they will buy
#    Then the program will compute how much the total amount is

#Step1 Ask how many apples the user wants to buy
#      and compute the cost
print("The price of apples and oranges are:\nApples: 20 pesos\nOranges: 25 pesos")

def askUser():
    appleCount = int(input("How many apples do you want to buy?:"))
    orangeCount = int(input("How many oranges do you want to buy?:"))
    return appleCount, orangeCount

#Step 2 Compute the price of apples and oranges and their total
def computePrice(appleCount_, orangeCount_):
    applePrice = appleCount_*20
    orangePrice = orangeCount_*25
    totalPrice = applePrice+orangePrice
    return totalPrice

appleCount, orangeCount = askUser()
totalPrice = computePrice(appleCount, orangeCount)