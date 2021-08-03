

def merge_sorted_array(arr_one, arr_two):
    new_array = arr_one + arr_two
    length = len(new_array) - 1
    i = 0
    while i < length:
        if new_array[i] > new_array[i + 1]:
            temp = new_array[i]
            new_array[i] = new_array[i + 1]
            new_array[i + 1] = temp
        else:
            i += 1
    print(new_array)





merge_sorted_array([0,3,4,31], [4,6,30])


