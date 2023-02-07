import random 

n = [random.randint(0,9) for i in range(110)]

# for i in range(100):
#     print(f"0.{n[i]}", end=" ")

for i in range(110):
    print(f"{n[i]}", end=" ")

# Auto-correlation
# 0.12 0.01 0.23 0.28 0.89 0.31 0.64 0.28 0.83 0.93 0.99 0.15 0.33 0.35 0.91 0.41 0.60 0.27 0.75 0.88 0.68 0.49 0.05 0.43 0.95 0.58 0.19 0.36 0.69 0.87