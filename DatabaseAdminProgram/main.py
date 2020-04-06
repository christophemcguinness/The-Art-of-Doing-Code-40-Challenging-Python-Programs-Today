print(":: Welcome to the Database Admin Program ::\n")

log_on_information = {
    "admin00": "password1",
    "admin01": "password1",
    "admin02": "password1",
    "admin03": "password1",
    "admin04": "password1",
    "tom": "password2",
}

username = input("Enter your Username: ").lower()

if username in log_on_information.keys():
    password = input("Enter your Password: ")

    if password == log_on_information[username]:
        print("\nWelcome back {0}".format(username))

        if "admin" in username:
            print("Heres your current database:\n")
            for x in log_on_information.keys():
                print("username: {0}\tPassword: {1}".format(x, log_on_information[x]))
        else:
            pwchange = input("Would you like to change you password? (Yes/No) ").lower()

            if pwchange == "yes":
                newpw = input(":: Note new password must be at least 8 characters long ::"
                              "\n"
                              "What would you like to change your password too? ")
                if len(newpw) >= 8:
                    log_on_information[username] = newpw
                    print("Thanks {0} your password has now been changed to {1}".format(username,
                                                                                        log_on_information[username]))
                else:
                    print("Sorry {0} the new password you've selected is too short".format(username))
            else:
                print("Thanks for logging in {0}, see you later, Good bye".format(username))
    else:
        print("\nThe password you've provided does not match our records.")
else:
    print("\nSorry, that username does not exist")
