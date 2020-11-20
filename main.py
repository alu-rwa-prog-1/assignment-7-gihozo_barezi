import Account_class

print("\nMOBILE MONEY ---WELCOME")
print("\n1) Login     2) Create account ")

# Login info

choice = input("\nYour choice: ")

# User choice is Login

if choice == "1":

    print("\nLogin ----")
    phonenbr = input("\nPhone number: ")
    password = input("Password: ")

    # Check on login

    if phonenbr == Account_class.Account1.phonenbr and password == Account_class.Account1.password \
        or phonenbr == Account_class.Account2.phonenbr and password == Account_class.Account2.password:
        print("\nLogged in successfully ------")

        print("\nChoose the operation you want to make:")
        print("1) Transfer")
        print("2) Buy")
        print("3) Pay")
        print("4) Deposit")
        print("5) View Balance")
    else:
        print("That account doesn't exist")

# User choice is Create account

if choice == "2":

    print("Create account -----")


