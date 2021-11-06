#This program will ask the user the amount of money
#     and the current price of apples
#     The program will calculate the maximum number of 
#     how many apples the use can buy and compute the change

#Step1 Ask the amount of money the user have
def askUser():
    money = int(input("How much money do you have?: "))
    applePrice = int(input("What is the current cost of apples?: "))
    return money, applePrice

#Step2 Calculate the maximum number of apples the money can buy
def maxApples(money_, applePrice_):
    maxNumber = money_//applePrice_
    return maxNumber

#Step3 Calculate the change
def moneyChange(money_, applePrice_):
    change = money_%applePrice_
    return change

#Step4 Let the user know the maximum number of apples the money can buy
#      and the change
def userKnow():
    print(f"You can buy {maxBuy} apples and your change is {appleChange} pesos.")

money, applePrice = askUser()
maxBuy = maxApples(money, applePrice)
appleChange = moneyChange(money, applePrice)
userKnow()