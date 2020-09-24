from numpy import *

def bubble_sort(arr):

    for i in range(arr.size):
        for j in range(0,arr.size-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    print(arr)


arr=array([99,0,4])

bubble_sort(arr)

