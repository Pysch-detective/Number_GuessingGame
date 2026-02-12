# with open("passwords.txt", "a") as fi:
#     pin = input(
#         "Enter ur four digit pin to continue: "
#     )  # file only takes string values
#     fi.write(pin, "\n")

# services = ["Check Balance", "Deposit", "Withdraw", "Exit"]
while True:
    pin = input("Enter ur four digit to  continue: ")
    if len(pin) != 4 or not pin.isdigit():
        print("u have entered wrong pin")
    else:
        print("u have entered correct pin")
        break
Balance = 10000
print(
    "please Choose Banking services to continue \n",
    "1.Check Balance",
    "2.Deposit",
    "3.Withdraw",
    "4.Exit",
)

while True:
    try:
        options = int(input("Enter the input: "))

        if options == 1:
            print(f"Your balance is {Balance} ")
        elif options == 2:
            Deposit = int(input("Enter the amount u want to deposit?: "))
            Balance = Deposit + Balance
            print("Your amount Deposited Succesfully")
        elif options == 3:
            withdraw = int(input("Enter the amount u want to withdraw"))
            Balance = Balance - withdraw
            print("U have Succesfully withdrawed")
        else:
            print("Thank u for choosing ATM Services")
            break
    except ValueError:
        print("Please Choose from the options")
