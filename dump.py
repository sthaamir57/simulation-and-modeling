import random 

n = [random.randint(0,9) for i in range(110)]

# for i in range(100):
#     print(f"0.{n[i]}", end=" ")

for i in range(110):
    print(f"{n[i]}", end=" ")