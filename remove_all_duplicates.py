# Python 3 code to demonstrate
# removing duplicated from list
# using naive methods initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))

# using naive method
# to remove duplicated
# from list
res = []
for i in test_list:
    if i not in res:
        res.append(i)

# printing list after removal
print ("The list after removing duplicates : " + str(res))



# List comprehension
# Python 3 code to demonstrate
# removing duplicated from list
# using list comprehension

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))

# using list comprehension
# to remove duplicated
# from list
res = []
[res.append(x) for x in test_list if x not in res]
# printing list after removal
print ("The list after removing duplicates : " + str(res))


# Set
# Python 3 code to demonstrate
# removing duplicated from list
# using list comprehension

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))

# using list comprehension
# to remove duplicated
# from list
res = []
[res.append(x) for x in test_list if x not in res]

# printing list after removal
print ("The list after removing duplicates : " + str(res))



#
# List comp and enumerate
# Python 3 code to demonstrate
# removing duplicated from list
# using list comprehension + enumerate()
#
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))

# using list comprehension + enumerate()
# to remove duplicated
# from list
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]

# printing list after removal
print ("The list after removing duplicates : " + str(res))







# collectios.orderedDict.fromkeys()
# Python 3 code to demonstrate
# removing duplicated from list
# using collections.OrderedDict.fromkeys()
from collections import OrderedDict

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))

# using collections.OrderedDict.fromkeys()
# to remove duplicated
# from list
res = list(OrderedDict.fromkeys(test_list))

# printing list after removal
print ("The list after removing duplicates : " + str(res))