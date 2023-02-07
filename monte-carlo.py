import random

n = int(input("Enter number of iterations : "))
count = 0

for i in range(n):
    x = random.random()
    y = random.random()

    if x*x + y*y <= 1:
        count += 1

pi_calc = 4 * count / n

print("Estimated value of PI:", pi_calc)