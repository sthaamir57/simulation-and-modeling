def lcg(Xs,a,c,m):
    X = 0
    X = (Xs * a + c) % m
    return X

def main():
    choice = input("Choose\n1. Additive LCG\n2. Multiplcative LCG\n3. Mixed LCG\n4. Exit.\n\nChoice\t:\t")

    print("\n")
    if choice == '1':
        a = 1
        c = int((input("Enter value of 'c'\t:\t")))
    elif choice == '2':
        a = int(input(("Enter value of 'a'\t:\t" )))
        c=0
    elif choice == '3':
        a = int(input(("Enter value of 'a'\t:\t " )))
        c = int((input("Enter value of 'c'\t:\t ")))
    elif choice == '4':
        exit(0)
    else:
        print("Error")
        exit(0)
    Xs = int(input("Enter seed\t\t:\t"))
    m = int(input("Enter value of 'm'\t:\t"))
    n = 0
    print("\n\nGenerated Random Numbers\n")
    while(n<m):
        Xs = lcg(Xs,a,c,m)
        print(Xs, end=",")
        n += 1

main()