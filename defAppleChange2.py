#This program will ask the user the amount of money
#     and the current price of apples
#     The program will then calculate the maximum number of 
#     how many apples the use can buy and compute the change

#Step1 Ask the amount of money the user have
def askUser():
    moneyNumber = int(input("How much money do you have?: "))
    applePrice = int(input("What is the current cost of apples?: "))
    return moneyNumber, applePrice

#Step2 Calculate the maximum number of apples the money can buy
#      and the change
def maxApples(money_, applePrice_):
    maxNumber = money_//applePrice_
    appleChange = money_%applePrice_
    return maxNumber, appleChange

#Step3 Let the user know the maximum number of apples the money can buy
#      and the change
def userKnow():
    print(f"You can buy {maxNumber} apples and your change is {appleChange} pesos.")

moneyNumber, applePrice = askUser()
maxNumber, appleChange = maxApples(moneyNumber, applePrice)
userKnow()