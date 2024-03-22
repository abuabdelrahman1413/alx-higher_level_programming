#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    itr = 0
    counter = len(my_list)
    for i in range(counter):
        itr = itr + my_list[i][1]
    sum = 0
    for i in range(counter):
        sum += my_list[i][0] * my_list[i][1]
    avg = sum / itr
    return avg
