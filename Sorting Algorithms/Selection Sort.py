# Created by Moontasir Abtahee at 5/19/2023
# A simple implementation of Selection Sort Algorithm
# it worls by repeatedly finding the minimum element from unsorted part and putting it at the beginning


def selectionSort(arr):
    for i in range(len(arr)):
        min = findMin(arr,i)
        if(min!=i):
            swap(arr,i,min)
    return arr

def findMin(arr,i):
    #finding the min element from i to end
    min = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            min = j
    return min

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]






arr = [7,68,11,62,.2,226,35,0,35,-25,-22,45,-100]
print(selectionSort(arr))


# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Stable: No
    # Stable means that the relative order of elements with equal values is preserved after sorting.

