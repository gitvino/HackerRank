
'''
URL: https://www.hackerrank.com/challenges/organizing-containers-of-balls

'''

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    size = len(container)
    row_sum = []
    col_sum = []

    for index in range(size):
        col_sum.append(sum(row[index] for row in container))
        row_sum.append(sum(container[index]))

    row_sum.sort()
    col_sum.sort()

    if row_sum == col_sum:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':

    q = int(input())
    for q_itr in range(q):
        n = int(input())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        result = organizingContainers(container)
        print(result + '\n')

