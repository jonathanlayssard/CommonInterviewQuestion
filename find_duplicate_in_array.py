# def Repeat(x):
#     _size = len(x)
#     repeated = []
#     for i in range(_size):
#         k = i + 1
#         for j in range(k, _size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated
#
# # Driver Code
# list1 = [10, 20, 30, 20, 20, 30, 40,
#          50, -20, 60, 60, -20, -20]
# print (Repeat(list1))






# from collections import Counter
# 
# l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
# d = Counter(l1)
# print(d)
# 
# new_list = list([item for item in d if d[item]>1])
# print(new_list)