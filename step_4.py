import time
import pandas as pd
import numpy as np
'''imports the module which is a written program and provides a lot of built-in function'''
def elements(sub_elements,all_elements):
    '''Gives the return of length of verified elements'''
    start = time.time()
    verified_elements = []

    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)
    '''prints the length of verified elements and duration of execution using time function'''
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))



def usingnumpy():
   '''Using numpy vectorisation to fast the execution of the code''' 
    start = time.ti
    verified_elements = []
    elements = elements.intersect1d(subset_elements,all_elements)
'''Prints the length of verified elements and duration of execution using time function'''
print(len(verified_elements))
print('Duration: {} seconds'.format(time.time() - start))


def elements(sub_elements, all_elements):
    '''using a datastrucutre map() to speed the execution of code'''
    start = time.time()
    map(str(all_elements,verified_list))
'''prints the length of the verified_elements and duration of execution using time function'''
print(len(verified_elements))
print('Duration: {} seconds'.format(time.time() - start))
'''we can see that using numpy executes the fastest and then map and then for loop'''
