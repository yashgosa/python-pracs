"""Programs to separate and print ODD and EVEN numbers from array.
Also display Sum of all perfect numbers present in array at the end.
(Define Class and Methods in Class as per need)
Write a Python program to print all unique values in a dictionary.
"""
import functools
def get_arr():
    x = int(input("enter the size of array"))
    l = []
    for i in range(x):
        l.append(int(input("Enter the value")))
    return l

def get_odd_even():
    listx = get_arr()
    even = list(filter(lambda x: x % 2 == 0, listx))
    odd = list(filter(lambda x: x % 2 == 1, listx))
    perfect_num_sum = get_perfect_num(listx)
    return even, odd, perfect_num_sum

def get_perfect_num(listx):
    perf = []
    for ele in listx:
        result = 0
        for i in range(1, ele):

            if ele % i == 0:
                result += i
        if result == ele:
            perf.append(ele)
    print(perf)
    try:
        return functools.reduce(lambda x, y: x + y, perf)
    except TypeError:
        return "No perfect Numbers"
def get_dict():
    flag = True
    dictx = {}
    while flag:
        k, v = input("Enter the (key, value) pair ").split(", ")
        dictx.update({k: v})
        acc = input("Done? ").lower()
        if acc == "yes":
            flag = False

    return dictx
def get_unique():
    dictx = get_dict()
    l = []
    for k, v in dictx.items():
        if int(v) == 1:
            l.append(k)
    return l

if __name__ == "__main__":
    print(get_unique())
    print(get_odd_even())
