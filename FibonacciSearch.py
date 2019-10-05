# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:22:26 2019

@author: danie
"""

def FibSearch(ar, find):
    """n= size of the array

    Search starts looking at the element at the Fkth location. Here Fk≥n and Fk-1<n.

    While the binary search has low, high and mid positions, here we have mid=n-F(k-1)+1, F1=Fk-2, and F2=Fk-3.
    """
    n = len(ar)

 
    fib = fibSeq(n)
    print(fib)
    
    
    if n == 0:
        print("There is nothing within this list... cannot search for", find)
        return -1
    
    #elif (Fk >= n and F1 < n and n > 3):
    elif (n >= 1):
        k = len(fib) - 1 
        
        Fk = fib[k-1]
        F1 = fib[k-2]
        F2 = fib[k-3]
        
        mid = min(n - F1 + 1, len(ar)-1)
        
        print("Fk", Fk, "F1", F1, "F2", F2)
        print("Mid", mid, ar[mid])

        while ( 0 <= mid < len(ar) and ar[mid] != find and k > 0): 
       
            print("Mid", mid, "F1", F1, "F2", F2)
            if ar[mid] < find:
                print("Greater than")
                if F1 == 0: #Make sure it works
                    print("F1 = 1")
                    break
                else:
                    mid = mid + F2
                    F1 = fib[k - 2]
                    F2 = fib[k - 3]
                    k -= 2
                
            elif ar[mid] > find:
                print("Less than")
                if F2 == 0:
                    print("F2 = 0")
                    break
                else:
                    mid = mid - F2
                    F1 = fib[k - 2]
                    F2 = fib[k - 3]
                    k -= 1
        
        if ar[mid] == find:
            print(find, "was found at index", mid, "in", ar)
            return mid
            
        else:
            print(find, "was not found in within", ar)
            return -1

    else:
        print(find, "Was not found within", ar)
        return -1

def fibSeq(n): #Generation of Fibonacci sequence
    #where F1 is (k-1) and F2 is (k-2) and Fk is (k)
    F1 = 1
    F2 = 0 
    Fk = F1 + F2
    fib = [F2,F1, Fk]
   
    while (Fk < n): #Think this may need to chnage
        F2 = F1
        F1 = Fk
        Fk = F1 + F2
        fib.append(Fk)
        
    print("Fib", fib)
    return fib

def main():
    j0 = []
    j1 = [2] # Just work
    j2 = [1,2]
    j3 = [1,3,5]
    j = [2,3,6,4,8]
    j.sort()
    h = [34,56,900,87,123,456,27,4,8,0,145,2345]
    h.sort()
    print(j)
    print(FibSearch(j,2))
    #print(FibSearch(j, 6))
main()