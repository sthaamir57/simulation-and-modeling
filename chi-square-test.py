# get input from user
n = int(input("Enter number of data : "))

val_user = input('\nEnter space-separated data: ').split()

val = [float(item) for item in val_user]

c_val = float(input(f"\nEnter tabulated value : "))

observed = [0 for i in range(10)]
estimated = [10 for i in range(10)]
diff_squared=[0 for i in range(10)]

# find frequency of number in intervals
# int(0.11 * 10) => 1
# increment count in ovb[1] position
for num in val:
    observed[int(num*10)]+=1

diff_squared = [(pow(observed[i]-estimated[i], 2))/estimated[i] for i in range(10)]

c_calc = sum(diff_squared)

print(f'Class\t Observed\t Estimated\t ((Oi-Ei)^2)/Ei')
for i in range(10):
    print(f'{i+1}\t {observed[i]}\t\t {estimated[i]}\t\t {diff_squared[i]}')


if (c_calc < c_val):
    print("\n\nThe numbers are uniformly distributed")

else:
    print("\n\nThe numbers are not uniformly distributed")