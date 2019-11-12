def AtmTransactions():
    acountbal = 50000
    choice = input("Please enter 'b' to check balance, 'd' to deposit, 'w' to withdraw or 'q' to quit: ")
    while choice != 'q':
        if choice.lower() in ('w','d','b'):
            if choice.lower() == 'b':
                print("Your balance is: %d" % acountbal)
                print("Anything else?")
                choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                print(choice.lower())
            elif choice.lower() == 'd':
                deposit = float(input("Enter amount to deposit:"))
                acountbal = acountbal + deposit
                print("Anything else?")
                choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                print(choice.lower())
            else:
                withdraw = float(input("Enter amount to withdraw: "))
                if withdraw <= acountbal:
                    print("here is your: %.2f" % withdraw)
                    acountbal = acountbal - withdraw
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                else:
                    print("You have insufficient funds: %.2f" % acountbal)
        else:
            print("Wrong choice!")
            choice = input("Please enter 'b' to check balance, 'd' to deposit or 'w' to withdraw: ")
            
AtmTransactions()