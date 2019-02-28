# Ficonacci Numbers in a list and an Numpy array
# Python v3.6
# 2/28/2019


import numpy as np

def get_fibonacci_list(m, s):
    l = list(s)
    i = 0
    while i < m:
        l.append(l[i] + l[i+1])
        i += 1
    return l

def get_fibonacci_array(m, s):
    a = np.array(s)
    i = 0
    while i < m:
        a = np.append(a, a[i] + a[i+1])
        i += 1
    return a

def get_fibonacci_container(m, s):
    pass


def main():
    max_elements = 20 # the two seed elements are subtracted from this max_element
    two_seed_elements = (1,2)
    
    fibonacci_list = get_fibonacci_list(max_elements - 2, two_seed_elements) 
    print(f'fibonacci_list: {fibonacci_list}')
    print(f'len(fibonacci_list): {len(fibonacci_list)}')
    print(type(fibonacci_list))
        
    fibonacci_array = get_fibonacci_array(max_elements - 2, two_seed_elements)
    print(f'fibonacci_array: {fibonacci_array}')
    print(f'len(fibonacci_array): {len(fibonacci_array)}')
    print(type(fibonacci_array))
   
        
if __name__ == '__main__':
    main()