def authenticate():
    password = "keerthi15"
    attempts = 3

    while attempts>0:
        user_input = input("enter the password:")

        if user_input == password:
            print("Welcome!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong password! you have {attempts} attempts left.")
            else:
                print("Account blocked.")
                break


authenticate()