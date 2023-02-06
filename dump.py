import random 

n = [random.randint(0,95) for i in range(100)]

for i in range(100):
    print(f"0.{n[i]}", end=" ")