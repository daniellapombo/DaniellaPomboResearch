# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:52:43 2019

@author: danie
"""

import timeit
import random

#Generetes a list compossed of randomly generated integers
def randList(wrst = False, bst = False, av = True):
    if wrst:
        worst = [random.randint(0, 100000) for k in range(10000)]
        worst.sort(reverse = True)
        return worst
    if bst:
        best = [random.randint(0, 100000) for k in range(10000) ]
        best.sort()
        return best
    if av:
        avg = [random.randint(0, 100) for k in range(10)]
        return avg
 
def b_index(m,val, leng):
    #floor(val/divider)
    #ceil((max+1)/len(bucket))
    return int((val//((m+1)/leng)))    
    
def bucketSort(ar):
    # m = max
    #ar = input array
    arr_L = len(ar)
    b_list = []
    arr_max = max(ar)
    
    for k in range(len(ar)-1):
        b_list.append([])
    
    for k in ar:
        b_list[b_index(arr_max, k, arr_L-1)].append(k)
    
    for B in b_list:
        if len(B)<1:
            break
        else:
            b_list[b_list.index(B)] = insertionSort(B)
        
    index = 0
    for B in b_list:
        for k in range(len(B)):
            ar[index] = B[k]
            index += 1
            
    return ar
    
def needSorting(ar):
    #True indicates NEEDS sorting and False indicates is already sorted doesnt need sorting
    yes = False
    for k in range(len(ar)-1):
        if ar[k]>ar[k+1]:
            yes = True
            index = k #Key is the last position of the sorted list
            break
    if yes:
        return (yes,index)
    else:
        return(yes, -1)

def insertionSort(ar):
    for i in range(1,len(ar)):
        temp = ar[i]
        index = i
        while (index > 0 and ar[index-1] > ar[index]):
            ar[index] = ar[index-1] 
            index -= 1
            ar[index] = temp #Same as ar[index], ar[index-1] = ar[index-1], ar[index]
        
    return ar

#Function that swaps to values from different postions w/in list
def swap(ar, in1, in2):
    v1 = ar[in1]
    v2 = ar[in2]
    
    temp = v2
    ar[in2] = v1
    ar[in1] = temp
    
    #returns edited list after swap
    return ar
    
#Iterate through whole list bubble by bubble (bubble size decreases each epoch)
def bubbleSort(ar):
    for k in range(len(ar), 0, -1):
        for i in range(1,k) :
            if (ar[i]<ar[i-1]):
                swap(ar, i-1, i) #swap neighbors that are out of order
    return ar

def selectSort(ar):
    for k in range(1,len(ar)): 
        max_index = 0 #Select max
        for i in range(1, len(ar)):
            if ar[max_index] < ar[i]: #Find max
                max_index = i # If find new max, lab it as the new max
            swap(ar, max_index, i) #Swap the old max and the new max
    return ar


# Python program for implementation of MergeSort given by Dr. Putonti in class
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        i = j = k = 0
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
            
    return arr

def time_merge():
    st = 'from __main__ import mergeSort '
    sp = str(randList(wrst = False, bst = False, av = True))
    T = timeit.timeit(stmt = st, setup = sp)
    print("Merge Sort average case", T)
    return T

def time_sort():
    """def time_sort():
    st = 'ar.sort()'
    sp = 'ar = [120, 3, 76, 89, 11, 345]'
    T1 = timeit.timeit(stmt=st, setup=sp)
    print(T1)
    return T1"""
    
    st = str(randList(wrst = False, bst = False, av = True).sort())
    sp = str(randList(wrst = False, bst = False, av = True))
    T = timeit.timeit(stmt = st, setup = sp)
    print("TimeSort average case", T)
    return T

def time_insertion_Best():
    st = 'from __main__ import insertionSort '
    rd = randList(wrst = False, bst = True, av = False)
    #insertionSort(ar, isSorted)
    sp = str(rd, needSorting(rd))
    T= timeit.timeit(stmt = st, setup = sp)
    print("Insertion sort best case", T)
    return T

def time_insertion_Worst():
    st = 'from __main__ import insertionSort '
    rd = randList(wrst = True, bst = False, av = False)
    #insertionSort(ar, isSorted)
    sp = str(rd, needSorting(rd))
    T= timeit.timeit(stmt = st, setup = sp)
    print("Insertion sort worst case", T)
    return T

def time_selection_Best():
    st = 'from __main__ import insertionSort '
    sp = str(randList(wrst = False, bst = True, av = False))
    T = timeit.timeit(stmt = st, setup = sp)
    print("Selection sort best case", T)
    return T

def time_selection_Worst():
    st = 'from __main__ import insertionSort '
    sp = str(randList(wrst = True, bst = False, av = False))
    T = timeit.timeit(stmt = st, setup = sp)
    print("Selection sort worst case", T)
    return T

def time_bubble_Best():
    st = 'from __main__ import bubbleSort '
    sp = str(randList(wrst = False, bst = True, av = False))
    T = timeit.timeit(stmt = st, setup = sp)
    print("Bubble sort best case", T)
    return T

def time_bubble_Worst():
    st = 'from __main__ import bubbleSort'
    sp = str(randList(wrst = True, bst = False, av = False))
    T = timeit.timeit(stmt = st, setup = sp)
    print("Bubble sort worst case", T)
    return T

if __name__ == "__main__":
    
    pickSort = input("Enter in sorting algorithm wish to implement ").lower().replace(" ", "")
    
    genTime = input("Would you like to generate the time? Yes or No ")
    print("")
    
    List = randList(wrst = False, bst = False, av = True)
    
    print("Unsorted list:", List)
    
    if pickSort == "merge" or pickSort == "mergesort":
        print("Sorted list:", mergeSort(List))
        
    if pickSort == "insertion" or pickSort == "insertionsort":
        print("Sorted list:", insertionSort(List))
    
    if pickSort == "selection" or pickSort == "selectionsort":
        print("Sorted list:", selectSort(List))
        
    if pickSort == "bubble" or pickSort == "bubblesort":
        print("Sorted list:", bubbleSort(List))
        
    if pickSort == "time" or pickSort == "timesort":
        print("Sorted list:", List.sort())
        
    if pickSort == "bucket" or pickSort == "bucketsort":
        print("Sorted list:", bucketSort(List))
    
    if genTime.lower() == "yes":
        if pickSort == "merge" or pickSort == "mergesort":
            time_merge()
            
        if pickSort == "insertion" or pickSort == "insertionsort":
            time_insertion_Best()
            time_insertion_Worst()
        
        if pickSort == "selection" or pickSort == "selectionsort":
            time_selection_Best()
            time_selection_Worst()
            
        if pickSort == "bubble" or pickSort == "bubblesort":
            time_bubble_Best()
            time_bubble_Worst()
            
        if pickSort == "time" or pickSort == "timesort":
            time_sort()
    
