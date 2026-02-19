import re

print("Create Account")
password_pattern = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
)
username = input("Enter your username: ")
while True:
    Password = input("Enter ur pasword: ")
    if password_pattern.fullmatch(Password):
        print("Success! U have Strong password: ")
        break
    else:
        print("\n[Weak Password] Your password must contain:")
        print("- At least 8 characters")
        print("- Uppercase and lowercase letters")
        print("- At least one digit and one special character (@$!%*?&)\n")

with open("Passwords.txt", "a") as f:
    f.write(f"{username},{Password}\n")

sucess = False
chances = 3

while chances > 0:
    login_username = input("Enter ur username: ")
    login_Password = input("Enter ur Password: ")
    found = False
    with open("Passwords.txt", "r") as f:
        for line in f:
            stored_name, stored_password = line.strip().split(",")

            if login_username == stored_name and login_Password == stored_password:
                found = True
                break
    if found:
        print("U have Login Sucessfully")
        break
    else:
        chances -= 1
        if chances > 0:
            print(f"Incorrect. You have {chances} attempts left.\n")
        else:
            print("Access Denied. Out of attempts.")


else:
    print("U have Run out of chances")
