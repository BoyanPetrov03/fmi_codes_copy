# def selection_sort(A: list):
#     for index in range(len(A)):
#         min_index = index
#         for j in range(min_index+1, len(A)):
#             if A[j] < A[min_index]:
#                 j = min_index
#
#         A[index], A[min_index] = A[min_index], A[index]
#     return A
#
# print(selection_sort([-1,12,0,32,-4,-3,7,13]))
#

import pickle
import random