#This program will ask the user the amount of money
#     and the current price of apples
#     The program will then calculate the maximum number of 
#     how many apples the use can buy and compute the change

#Step1 Ask the amount of money the user have
#      and calculate the maximum number of apples the money can buy
#      and the change
def askingCompute():
    global moneyAmount
    moneyAmount = int(input("\nHow much money do you have?: "))
    global applePrice
    applePrice = int(input("How much are apples?: P"))
    def appleCompute():
        global appleCount 
        appleCount = moneyAmount//applePrice        
    def moneyChange():
        global appleChange
        appleChange = moneyAmount%applePrice
        
    appleCompute()
    moneyChange()

#Step2 Let the user know the maximum number of apples the money can buy
#      and the change
def userKnow():
    if moneyAmount<applePrice:
        print("\nNot enough money.")
    else:
        print(f"You can buy {appleCount} apples and your change is {appleChange} pesos.")

askingCompute()
userKnow()