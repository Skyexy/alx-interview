#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """ rotatae a 2d matrix 90 degrees clockwise."""
    lent = len(matrix)
    sem = [[matrix[j][i] for i in range(lent)] for j in range(lent)]
    height = lent - 1
    for i in range(lent):
        width = 0
        for x in range(lent)):
            matrix[x][i] = sem[height][width]
            width = width + 1
        height = height - 1
