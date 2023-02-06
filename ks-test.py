val = []
d = []
# get input from user
n = int(input("Enter number of data : "))
print("Enter data :")
for i in range(n):
    ele = float(input(f"data[{i+1}] : "))
    val.append(ele)
d_tab = float(input(f"Enter tabulated value : "))

val.sort();

for i in range(n):
    # d_plus
    j = ((i+1)/n) - val[i]
    d.append(j)

    # d_minus
    j = val[i] - (i/n)
    d.append(j)

# Max of D_plus and D_minus
d.sort(reverse=True)
d_calc = d[0];

if(d_calc <= d_tab):
    print(f"Since, D-calc ({d_calc}) <= D-tab ({d_tab})")
    print("The numbers are uniformly distributed")
else:
    print(f"Since, D-tab ({d_tab}) < D-calc ({d_calc})")
    print("The numbers are not uniformly distributed")