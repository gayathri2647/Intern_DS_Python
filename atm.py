print("Welcome to the Indian Bank ATM")
print("Please insert your ATM card to proceed.")
x= input("Insert your ATM card (y/n):")
if x=="y":
    print("Please enter your 4 digit pin number:")
    y= input("Enter your pin number:")
    if y=="1234":
        print("Please select your transaction:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Balance Inquiry")
        print("4. Exit")
        z= input("Enter your choice (1/2/3/4):")
        if z=="1":
            print("Please enter the amount to be withdrawn:")
            a= input("Enter the amount:")
            print("Please collect your cash.")
            print("Thank you for using Indian Bank ATM.")
        elif z=="2":
            print("Please enter the amount to be deposited:")
            b= input("Enter the amount:")
            print("Your amount has been deposited successfully.")
            print("Thank you for using Indian Bank ATM.")
        elif z=="3":
            print("Your account balance is 10000.")
            print("Thank you for using Indian Bank ATM.")
        elif z=="4":
            print("Thank you for using Indian Bank ATM.")
            print("Please collect your ATM card.")
else:
    print("Invalid Pin number. Please try again.")
    print("Thank you for using Indian Bank ATM.")
