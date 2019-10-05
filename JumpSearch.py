# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:22:09 2019

@author: danie
"""
import math

def jumpJS(low,high):
    #“jump” is defined as the square root of the length of the list.
    if (high - low) == 0: #If differnce is 0 return 0 (save time and computations)
        return 0
    else:
        return int(math.sqrt(high - low))
    
def classJumpSearch(ar, find):
    #Initialize low, high and step size j
    
    n = len(ar) #Length of the input array ar
    flag = 0 #Indication that found the value find
    low = 0 #Lower bound of interval
    high = n - 1 #Upper bound of interval
    j = low 
    position = 0
    #jumpJS(low,high) is the step size
    if n > 0:
        while(low <= high and flag == 0): #While have not found value find
            j = low + jumpJS(low,high)  #Update jth value by step size
        
            if ar[j] == find: #Found the value find
                flag = 1 #Indication find was found
                position = j #Index of find with array
                
            else:
                if ar[j] < find: #find is in the upper half of the interval
                    #update the upper bound of the interval to j + 1
                    low = j + 1
                    
                elif ar[j] > find: #find is in the lower half of the interval
                    #update the upper bound of the interval to j - 1 (cuz k its not at mid)
                    high = j - 1
                   
        if flag == 1: #Found value find
            print(find, "was found at index ", position)
            return j
        
        else: #Have not found the value find
            print(find, "was not found")
            return -1
    else:
        print("Array is empty could not perform search")
        return -1
    
def main():
    e = []
    j = [2,3,6,4,8]
    h = [34,56,900,87,123,456,27,4,8,0,145,2345]
    
    j.sort()
    h.sort()
    
    classJumpSearch(h,2345)
main()