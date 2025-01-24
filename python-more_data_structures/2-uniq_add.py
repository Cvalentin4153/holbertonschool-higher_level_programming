#!/usr/bin/python3

def uniq_add(my_list=[]):
    values = []
    total = 0
    for num in my_list:
        if num not in values:
            values.append(num)
            total += num
    return total
