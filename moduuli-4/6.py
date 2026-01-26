import random
N = int(input("Anna satunnaispisteiden määrä: "))
n = 0   # ympyrän sisään osuvien pisteiden määrä
i = 0   # laskuri
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    i += 1
pi_approx = 4 * n / N
print(f"π:n likiarvo satunnaispisteillä: {pi_approx}")
