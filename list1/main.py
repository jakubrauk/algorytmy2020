from math import fabs
import numpy as np
from random import randrange, randint
import matplotlib.pyplot as plt

def randomGrade(start, stop, step):
    return randint(0, int((stop - start) / step)) * step + start


def createMatrix(row_quant, col_quant):
    """
    Return row_quant x col_quant dimensional np.array filled with random grades
    """
    matrix = []
    for j in range(0, row_quant):
        row = []
        for i in range(0, col_quant):
            row.append(randomGrade(2.0, 5.5, 0.5))
        matrix.append(row)
    np_matrix = np.array(matrix)
    return np_matrix


def howManyFailed(matrix, n):
    """
    Returns number of students (from matrix) that have failed at least n courses
    """
    students = 0
    for student in matrix:
        failed_courses = 0
        for grade in student:
            if grade < 3:
                failed_courses += 1
        if failed_courses >= n:
            students += 1
    return students


def averageGrade(student):
    """
    returns avarege grade of a student (row in matrix)
    """
    return np.average(student)


def maxAverage(matrix):
    """
    returns a list of grades of the best student (best = max(averageGrade()))
    """
    average_grades = []
    for student in matrix:
        average_grades.append(averageGrade(student))
    average_grades_obj = np.array(average_grades)
    return matrix[average_grades_obj.argmax()]

def minAverage(matrix):
    """
    returns a list of grades of the best student (best = max(averageGrade()))
    """
    average_grades = []
    for student in matrix:
        average_grades.append(averageGrade(student))
    average_grades_obj = np.array(average_grades)
    return matrix[average_grades_obj.argmin()]

def allmax(a):
    """
    returns all max values (indexes) from array
    """
    if len(a) == 0:
        return []
    all_ = [0]
    max_ = a[0]
    for i in range(1, len(a)):
        if a[i] > max_:
            all_ = [i]
            max_ = a[i]
        elif a[i] == max_:
            all_.append(i)
    return all_

def theBestStudent(matrix):
    """
    returns student with the highest number of the best grades
    """
    highest_grade = matrix.max()
    how_many_grades = []
    for student in matrix:
        counter = 0
        for grade in student:
            if grade == highest_grade:
                counter += 1

        # if student.max() == highest_grade:
        #     counter += 1
        how_many_grades.append(counter)
    how_many_grades = np.array(how_many_grades)
    return matrix[np.array(allmax(how_many_grades))]


def studentsBetterThan(matrix, param):
    """
    returns np.array of students that average grade is >= param
    """
    students_average = []
    for student in matrix:
        students_average.append(averageGrade(student))
    students_average = np.array(students_average)
    list_of_students = []
    for i in range(0, len(students_average)):
        if students_average[i] >= param:
            list_of_students.append(i)
    return matrix[list_of_students]

def symDistance(a, b):
    """
    Returns symetrical distance between 2 matrices (of the same dimensions)
    """
    final_sum = 0
    for i in range(np.size(a, 0)):
        row_sum = 0
        for j in range(np.size(a, 1)):
            row_sum += fabs(a[i][j] - b[i][j])
        final_sum += row_sum
    return final_sum


def spacer():
    print('================')

def zad1_1(matrix):
    print('Zadanie 1.1:')
    n = int(input('Podaj n:'))
    number_of_students = howManyFailed(matrix, n)
    print(f'Liczba studentów, która nie zaliczyła conajmniej {n} przedmiotów: {number_of_students}')

def zad1_2(matrix):
    print('Zadanie 1.2:')
    print(f'Oceny studentów z najlepszą średnią: {maxAverage(matrix)}')
    print(f'Oceny studentów z najniższą średnią: {minAverage(matrix)}')

def zad1_3(matrix):
    print('Zadanie 1.3:')
    print('Oceny studentów z największą liczbą ocen najwyższych:')
    print(theBestStudent(matrix))

def zad1_5(matrix):
    print('Zadanie 1.5:')
    # n = int(input('Podaj n: '))
    n = 4.0
    print('Lista studentów ze średnimi nie mniejszymi niż 4.0:')
    print(studentsBetterThan(matrix, n))

def zad2():
    a = createMatrix(4,4)
    b = createMatrix(4,4)
    print('a:')
    print(a)
    print('b:')
    print(b)
    print(f'Odległośc symetryczna między macierzami a i b wynosi: {symDistance(a,b)}')

if __name__ == '__main__':
    x = createMatrix(4,4)
    print(x)
    # #Save histogram into file
    # plt.hist(x, bins=[2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])
    # plt.savefig('demo.png')

    zad1_1(x)
    spacer()
    zad1_2(x)
    spacer()
    zad1_3(x)
    spacer()
    zad1_5(x)
    spacer()
    zad2()

