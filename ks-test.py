d_tab = 0.565
val = [0.44, 0.81, 0.14, 0.05, 0.93]
val.sort();
n = len(val)
d=[]

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

if(d_calc < d_tab):
    print("The numbers are uniformly distributed")
else:
    print("The numbers are not uniformly distributed")