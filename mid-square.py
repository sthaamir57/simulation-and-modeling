import math

def midValues(seed):
    len_seed = len(str(seed))
    len_max = len_seed * 2
    seeds = []
    while 1:
        # find square of seed
        sq = int(seed) * int(seed)
        sq_str = str(sq)

        # add 0 form head if necessary
        if(len(str(sq)) < len_max):
            for i in range(len_max - len(sq_str)):
                sq_str = '0' + sq_str

        # extract seed value
        start = math.ceil(len(str(seed)) / 2)
        end = start + len_seed
        seed = int(sq_str[start : end])

        # stop if seed already exists or is zero
        if seed in seeds or seed == 0:
            seeds.append(seed)
            return seeds
        seeds.append(seed)

def main():
    seed = input("Enter the value of seed : ")
    RN = midValues(seed)
    print("Random number generated using mid square method :")
    [print(i) for i in RN]
    
main()