from random import randint
import time


def generateList(n):
    list_ = []
    for i in range (0, n):
        list.append(randint(0, 1001))
    return list_


def bubbleSort(list_):
    start = time.time()
    for i in range(len(list_)):
        for j in range(0, len(list_)-1):
            if list_[j] > list_[j+1]:
                temp = list_[j]
                list_[j] = list_[j+1]
                list_[j+1] = temp
    end = time.time()
    return list_, end - start
        

def ex1():
    n = int(input('Z ilu liczb ma się składać lista?: '))
    list_of_times = []
    for i in range(0, 10):
        list_ = generateList(n)
        sorted_list, time_diff = bubbleSort(list_)
        list_of_times.appen(time_diff)        



if __name__ == '__main__':
    L = generateList(10)
    for element in L:
        print(element)
