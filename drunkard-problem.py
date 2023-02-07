import random
pos = [0, 0]
pos_prev = str(pos)

print(f"S.No.\tInitial Position\tRandom Number\tMovement\tNext Position")

for i in range(20):
    random_num = int(random.randint(0,99))
    pos_prev = str(pos)

    if random_num in range(0, 24):
        pos[1]+=1
        movement = "forward"
    elif random_num in range(25, 49):
        pos[1]-=1
        movement = "backward"
    elif random_num in range(50, 74):
        pos[0]-=1
        movement = "left"
    elif random_num in range(75, 100):
        pos[0]+=1
        movement = "right"
    
    print(f"{i+1}\t{str(pos_prev):<16}\t{random_num:<13d}\t{movement:<9}\t{pos}")