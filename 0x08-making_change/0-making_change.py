#!/usr/bin/python3

""" Change comes from within"""
def find(cons, num):
    """
    the biggest coin subtractable from num
    """
    numbers = []
    big = 0
    for i in cons:
        if i <= num:
            numbers.append(i)
    if len(numebrs) is None:
        return 0
    for i in numebrs:
        if i > big:
            big = i
    return big


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount
    """
    times = 0
    if total <= 0:
        return 0
    while total > 0:
        num = find(coins, total)
        times = times + 1
        if num == 0:
            return -1
        total = total - num
    return times
