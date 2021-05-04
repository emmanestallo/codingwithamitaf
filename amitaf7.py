import random 
permu_list = []
str_inp = input('Enter String: ')
permu_list.append(list(str_inp))
def permu_ns(str_inp):
    x = random.randint(0,2)
    y = random.randint(0,2)
    z = random.randint(0,2)
    str_inp = list(str_inp)
    if x != y and x != z and y !=z:
        str_inp[0],str_inp[1],str_inp[2] = str_inp[x], str_inp[y], str_inp[z]
        if str_inp not in permu_list:
            permu_list.append(str_inp)
            permu_ns(str_inp)
    else:
        permu_ns(str_inp)

    while len(permu_list)<6:
        permu_ns(str_inp)


permu_ns(str_inp)
for i in range (len(permu_list)):
    permu_list[i] = "".join(permu_list[i])
print(permu_list)