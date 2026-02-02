def gallons_to_liters(g):
    return g * 3.785
gallons = 1
while gallons >= 0:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallons < 0:
        break
    liters = gallons_to_liters(gallons)
    print(f'{gallons:.2f} American gallons is {liters:.2f} liters.')
