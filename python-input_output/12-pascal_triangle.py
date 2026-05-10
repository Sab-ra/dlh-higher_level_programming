#!/usr/bin/python3
"""Pascal's Triangle String Representation"""


def pascal_triangle(n):
    """Returns list of lists for PT"""
    pt = []
    ending = [1]
    if n <= 0:
        return pt
    else:
        for i in range(n):
            pt.append([1])
    if n < 2:
        return pt
    else:
        core_slice = []
        for i in range(1, n):
            for j in range(1, len(pt[i-1])):
                core_slice.append((pt[i-1][j-1]) + (pt[i-1][j]))
                print(core_slice)
            pt[i] = pt[i] + core_slice + ending
            core_slice = []
        return pt
