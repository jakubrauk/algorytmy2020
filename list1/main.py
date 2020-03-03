import numpy as np
from random import randrange, randint


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



