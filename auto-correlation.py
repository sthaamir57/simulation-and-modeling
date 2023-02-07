from math import floor, sqrt

val_user = input('\nEnter (space-separated) data: ').split()
val = [float(item) for item in val_user]
i = int(input("Enter beginning position (i) : "));
val_arr = [i]
m = int(input("Enter gap or lag (m) : "))
N = len(val)
sum = 0
Zcalc = 1.96

M = floor((N-i)/m-1)

for j in range(M+1):
    val_arr.append(i+(j+1)*m)
for k in range(len(val_arr)-1):
    sum = sum + val[val_arr[k]-1]*val[val_arr[k+1]-1]

rho = (sum/(M+1))-0.25

sigma = sqrt(13*M+7) / (12 * (M+1))

Zo = rho/sigma

print("\nZo=", Zo)
print("Zcalc=", Zcalc)

if (Zo < Zcalc):
    print("\n\nThe numbers are independent.\n")
else:
    print("\n\nThe numbers are not independent.\n")