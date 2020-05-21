import random
import math

A = [2, 3, 63, 12, 56, 78, 22, 8]


def Quicksort(A, left=0, right=len(A) - 1):
    if left < right:
        # q = Partition(A, right, left)
        q = PartitionRandom(A, left, right)
        Quicksort(A, left, q - 1)
        Quicksort(A, q + 1, right)


def PartitionRandom(A, right, left):
    s = random.randint(right, left)
    A[left], A[s] = A[s], A[left]
    return Partition(A, right, left)


def Partition(A, right, left):
    x = A[left]
    i = right - 1

    for j in range(right, left):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[left] = A[left], A[i + 1]
    return i + 1


Quicksort(A)
for i in A:
    print('%.5f' % i)
