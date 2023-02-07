val_user = input('\nEnter 110 single digit 0-9 (space-separated) data: ').split()
val = [float(item) for item in val_user]
digits = [0,1,2,3,4,5,6,7,8,9]


def get_gaps(digit):
    indexes = []
    for ind,num in enumerate(val):
        if(num==digit):
            indexes.append(ind)

    gaps =[]


    for pos,ind in enumerate(indexes):
        if (pos+1)!=(len(indexes)):
            gap = (indexes[pos+1]-indexes[pos])-1
            gaps.append(gap)
    return gaps

all_gaps=[]

for digit in digits:
    for gap in get_gaps(digit):
        all_gaps.append(gap)

def gap_length_freq(a,b):
    freq = 0
    for i in range(a,b+1):
        for j in all_gaps:
            if(i==j):
                freq+=1
    return freq

max_class = max(all_gaps)

while(((max_class+1)%3)!=0):
    max_class+=1

def cum_freq(a,b):
    cf = gap_length_freq(a,b)/100

    while a!=0:
        a -= 4
        b -= 4
        cf += gap_length_freq(a,b)/100
    return cf

def func(b):
    x = b
    return (1 - 0.9 **(x+1))

classes = []

initial = [0,3]
val_ranks = []
while initial[1] < max_class+4:
    classes.append(initial)
    fx_sub_cf = abs(func(initial[1]) - cum_freq(initial[0],initial[1]))
    val_ranks.append(fx_sub_cf)

    print(f"{str(initial):>8}",gap_length_freq(initial[0],initial[1]),gap_length_freq(initial[0],initial[1])/100,f"{float(cum_freq(initial[0],initial[1])):5.2f}",f"{float(func(initial[1])):7.4f}",f"{fx_sub_cf:7.4f}",sep = "\t")
    initial[0] += 4
    initial[1] += 4

val_calc = max(val_ranks)
val_tab = 1.36/100

if (val_calc < val_tab):
    print("\n\nThe numbers are independent.")

else:
    print("\n\nThe numbers are not independent.")