observed = []
# user input
n = float(input("Enter total no. of data : "))
choice = input("\nChoose\n3. Three-digit\n4. Four-digit\n5. Five-digit\n0. Exit.\n\nChoose digit\t:\t")
print("\n")
if choice == '3':
    prob = [0.72, 0.01, 0.27]
    observed.append(float(input("All digits are same\t\t:\t")))
    observed.append(float(input("All digits are different\t:\t")))
    observed.append(float(input("One pair\t\t\t:\t")))
elif choice == '4':
    prob = [0.001, 0.504, 0.036, 0.027, 0.432]
    observed.append(float(input("All digits are same\t\t:\t")))
    observed.append(float(input("All digits are different\t:\t")))
    observed.append(float(input("Three like digits\t\t:\t")))
    observed.append(float(input("Two pairs\t\t\t:\t")))
    observed.append(float(input("One pair\t\t\t:\t")))
elif choice == '5':
    prob = [0.0001, 0.3024, 0.072, 0.0045, 0.072, 0.108, 0.504]
    observed.append(float(input("All digits are same\t\t:\t")))
    observed.append(float(input("All digits are different\t:\t")))
    observed.append(float(input("Three like digits\t\t:\t")))
    observed.append(float(input("Four like digits\t\t:\t")))
    observed.append(float(input("Full house (eg:11122, 11222)\t:\t")))
    observed.append(float(input("Two pairs\t\t\t:\t")))
    observed.append(float(input("One pair\t\t\t:\t")))
elif choice == '0':
    exit(0)
else:
    print("Error")
    exit(0)

if(sum(observed) != n):
    print("Error! Total count not equal to provided data.")
    print(sum(observed))
    exit(0)

val_tab = float(input("Enter tabulated value : "))

estimated = [float(num * n) for num in prob]
diff_squared = [(pow(observed[i]-estimated[i], 2))/estimated[i] for i in range(len(observed))]
val_calc = sum(diff_squared)

print("\nCombination\t Observed\t Estimated\t ((Oi-Ei)^2)/Ei")
for i in range(len(observed)):
    print(f"{i+1}\t\t {observed[i]}\t\t {estimated[i]}\t\t {diff_squared[i]}")

if (val_calc < val_tab):
    print("\n\nThe numbers are independent.")

else:
    print("\n\nThe numbers are not independent.")