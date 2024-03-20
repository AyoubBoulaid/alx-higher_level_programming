#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_num = set()
    for num in my_list:
        uniq_num.add(num)
    result = sum(uniq_num)

    return result
