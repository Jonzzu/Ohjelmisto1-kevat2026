count = 0
while count < 5:
    kayttaja = input('Enter username: ')
    salasana = input('Enter password: ')

    if kayttaja == "python" and salasana == "rules":
        print("Welcome")
        break
    else:
        count = count + 1
        if count < 5:
            print("Incorrect username or password. Please try again.")

if count >= 5:
    print("Access denied")