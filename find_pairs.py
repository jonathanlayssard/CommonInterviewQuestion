"""

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

1   2    4   15
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7    11

Sample input/output (pseudodata):

parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (15, 9),
    (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]

Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.

Output may be in any order:

find_nodes_with_zero_and_one_parents(parent_child_pairs) => [
  [1, 2, 4, 15],       # Individuals with zero parents
  [5, 7, 8, 11]        # Individuals with exactly one parent
]

n: number of pairs in the input
parents  children
1         3
2         3
3         6
5         6
15        9
5         7
4         5
4         8
4         9
9         11

"""

parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (15, 9),
    (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]


def func_parent_child_pair(parent_child_pairs):
    
    parent_list = []
    child_list = []
    
    freq = {}
    
    for data in parent_child_pairs:
        parent_list.append(data[0])
        child_list.append(data[1])
        
    
    for child in child_list:
        if child not in freq:
            freq[child] = 0
        freq[child] += 1
        
    print(freq)
    
    for parent in parent_list:
        if parent not in freq:
            freq[parent] = 0
    
    one_parent,no_parent  = [],[]
    
    for k, v in freq.items():
        if v == 1 :
            one_parent.append(k)
        if v == 0:
            no_parent.append(k)
    
    print(one_parent)
    print(no_parent)
    
    

    
        
        
func_parent_child_pair(parent_child_pairs)
    
    
