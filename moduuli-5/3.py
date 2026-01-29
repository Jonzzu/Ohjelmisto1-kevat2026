luku = int(input("Enter an integer: "))

if luku > 1:
    for i in range(2, luku):
        if luku % i == 0:
            print(f"{luku} is not a prime number.")
            break
    else:
        print(f"{luku} is a prime number.")
else:
    print(f"{luku} is not a prime number.")