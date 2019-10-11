# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 19:28:02 2019

@author: danie
"""

import random as rd
import math

def midCut(low, high): #find the middle value between an interval [low,high]
    if (high - low)%2 == 0: #if length of interval is even
        mid = (high - low)/2
    else: #if length of interval is odd
        mid = (high-low)//2
        
    return int(mid) #return an integer, Not float


def recursiveBS(arr, low, high, find):
    #low is the lowest index in the interval
    #high is the highest index in the interval
    #Find is the value are searching for
    #arr is the input array
    
    if len(arr) == 0:
        print("Input array is empty, unable to find element")
        return None
    
    if low != high: #Insure are not at list with length of 1 where low == high
        #midCut is size of the step
        mid = low + midCut(low, high) #incrementing the new mid index by the step size midCut

        if arr[mid] == find: #find was in the middle of arr
            return mid
        
        elif arr[mid] > find: #Find is in the lower half of the input array
            #Update interval to be the lower half of the previous interval
           
            """the high index is now updated to be the 1 index behind the mid (cuz have a conditional statement if its 
            arr[mid] so do not need high to include the mid index now cuz k find is not at mid)"""
            
            high = mid - 1 
            
            return recursiveBS(arr,low,high,find) #now apply recursiveBS to the new interval
            
        elif arr[mid] < find:#Find is in the upper half of the input array
            #Update interval to be the upper half of the previous interval
            
            """the low index is now updated to be the 1 index after the mid (cuz have a conditional statement if its 
            arr[mid] so do not need low to include the mid index now cuz k find is not at mid)"""
            
            low = mid + 1
            
            return recursiveBS(arr,low,high,find)
            
        else:
            return -1 #did not find the value find in the array arr
        
    elif low == high: #In the case the arr/interval is of length 1
        if arr[low] == find: #If find is the only value in the length 1 interval
            return low
        
        else:
            return -1 #did not find the value find
        
def binarySearch(ar, find):
    #initialize low,high and mid values
    
    if len(ar) == 0:
        print("Input array is empty, unable to find element")
        return None
    
    low = 0
    high = len(ar)
    mid = midCut(low,high)
    
    #While the interval length is not of size 1 and have not found the index where the value find is
    while (ar[mid] != find and low < high):
        
        if (find < ar[mid]): #find is in the lower half of the interval
            
            high = mid -1 #update the upper bound of the interval to mid - 1 (cuz k its not at mid)
            low = low
            mid = high - midCut(low,mid-1) #update mid value: is mid value of new interval
            
            
        elif (find > ar[mid]): #find is in the upper half of the interval
            
            low = mid + 1 #update lower bound of the interval to mid + 1 (cuz k its not at mid)
            high = high
            mid = low + midCut(mid+1,high) #update mid value: is mid value of new interval
            
    if ar[mid] == find: #Found value at either ar[mid] and or ar[low] == ar[high]
        return mid
    
    else:
        return -1 #Did not find value
    
def classBinarySearch(ar, find):
    
    #initalize n, flag, low, high, mid and position
    n = len(ar) #Length of array
    flag = 0 #indicates if found find
    low = 0 #Lower bound of interval
    high = n -1 #Upper bound of interval
    mid = low #Middle index of interval
    position = 0 #Where find is
    if (n > 0):
        while(low <= high and flag == 0): #While have NOT found value find
            
            mid = low + midCut(low,high) #Update mid index to middle index of new interval
        
            if ar[mid] == find: #Found value...lucky!
                flag = 1 #Indicate was found
                position = mid #Indicate find's position
                print(find, "was found at index ", position)
                return position
                
            else:
                if ar[mid] < find: #find is in the upper half of the interval
                    #update lower bound of the interval to mid + 1 (cuz k its not at mid)
                    low = mid + 1
                    
                elif ar[mid] > find: #find is in the lower half of the interval
                    #update the upper bound of the interval to mid - 1 (cuz k its not at mid)
                    high = mid - 1
        
        if flag != 1: #Did not find value find
            print(find, "was not found")
            return -1
    else:
        print("Array is empty could not perform search")
        return -1
        
def main():
    #!!!Empty case
    e = []
    y = [3,5]
    j = [2,3,6,4,8]
    h = [34,56,900,87,123,456,27,4,8,0,145,2345]
    j.sort()
    h.sort()
    print(classBinarySearch(h,2345)) #Good
    print(recursiveBS(h, 0, len(h), 56))
    print(binarySearch(h, 56))
main()
