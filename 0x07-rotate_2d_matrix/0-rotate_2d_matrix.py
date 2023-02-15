#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """ rotatae a 2d matrix 90 degrees clockwise."""
    sem = [[matrix[j][i] for i in range(len(matrix))] for j in range(len(matrix))]
    height = len(matrix) - 1
    for i in range(len(matrix)):
        width = 0
        for x in range(len(matrix)):
            matrix[x][i] = sem[height][width]
            width = width + 1
        height = height - 1
