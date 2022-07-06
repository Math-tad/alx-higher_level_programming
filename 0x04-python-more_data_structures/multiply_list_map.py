#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def List(num, number):
        return num * number
    return list(map(List, my_list))
