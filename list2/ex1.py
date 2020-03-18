from random import randint
import time


def generateList(n):
    """
    Function returns a list with random generated integers from 0 to 1000
    """
    list_ = []
    for i in range (0, n):
        list_.append(randint(0, 1001))
    return list_


def average(list_):
    """
    returns average value of a list
    """
    sum = 0
    for element in list_:
        sum += element
    average = sum / len(list_)
    return average


def bubbleSort(list_):
    start = time.time()
    for i in range(len(list_)):
        for j in range(0, len(list_)-1):
            if list_[j] > list_[j+1]:
                temp = list_[j]
                list_[j] = list_[j+1]
                list_[j+1] = temp
    end = time.time()
    time_diff = end - start
    return list_, time_diff


def insertionSort(list_):
    start = time.time()
    for i in range(len(list_)):
        for j in range(0, i):
            if list_[i] < list_[j]:
                temp = list_[i]
                list_[i] = list_[j]
                list_[j] = temp
    end = time.time()
    time_diff = end - start
    return list_, time_diff


def ex1(n, algorithm='bubblesort'):
    # n = int(input('Z ilu liczb ma się składać lista?: '))
    list_of_times = []
    if algorithm == 'bubblesort':
        for i in range(0, 10):
            list_ = generateList(n)
            sorted_list, time_diff = bubbleSort(list_)
            list_of_times.append(time_diff)

        print('Najdluzszy czas sortowania (bubbleSort): %10.7f sekund'%max(list_of_times))
        print('Średni czas sortowania (bubbleSort): %10.7f sekund'%average(list_of_times))

    elif algorithm == 'insertionsort':
        for i in range(0, 10):
            list_ = generateList(n)
            sorted_list, time_diff = insertionSort(list_)
            list_of_times.append(time_diff)

        print('Najdluzszy czas sortowania (insertionSort): %10.7f sekund'%max(list_of_times))
        print('Średni czas sortowania (insertionSort): %10.7f sekund'%average(list_of_times))


if __name__ == '__main__':
    n = int(input('Z ilu liczb ma się składać lista?: '))

    ex1(n, algorithm='bubblesort')
    print('======================')
    ex1(n, algorithm='insertionsort')
