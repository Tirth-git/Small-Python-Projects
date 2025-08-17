def show_balance(balance):

    print(f"Your Balance is ₹{balance:.2f}")

def deposit():

    print("**************************************")
    amount = float(input("Enter an amount to be Deposited: "))
    if amount<0:
        print("That's not a Valid Amount")
        return 0
    else:
        return amount

def withdraw(balance):

    print("**************************************")
    amount = float(input("Enter an amount to be Withdrawn: "))

    if amount > balance:

        print("Insufficient Funds")
        return 0

    elif amount < 0:

        print("Amount must be greater than Zaro")
        return 0

    else:
        return amount

def main():
    balance= 0.00
    is_running=True

    while is_running == True:
        print("**************************************")
        print("Banking with SBI")
        print("1. Show Balance. \n2. Deposit. \n3. Withdraw. \n4. EXIT.")
        print("**************************************")
        choice = int(input("Enter your Choice (1-4): "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("Thats an invalid choice")

    print("**************************************")
    print("Thank you have a nice day")
    print("**************************************")

if __name__ == '__main__':
    main()