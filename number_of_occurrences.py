
my_list = [1,2,3,4,1,1,1,1]
my_dict = {}

def number_of_occurences():
    for index in my_list:
        if index not in my_dict:
            my_dict[index] = 1
        else:
            my_dict[index] = my_dict[index] + 1


number_of_occurences()

print(my_dict)