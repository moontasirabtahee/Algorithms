# Created by Moontasir Abtahee at 5/19/2023
# A simple implementation of Bubble Sort Algorithm

def bubbleSort(arr):
    flag = int()
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
                flag = 1
        if flag == 0:
            break
    return arr

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]


ar = [7,68,11,62,.2,226,35,0,35,-25,-22,45,-100]
print(bubbleSort(ar))


# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Stable: Yes
    # Stable means that the relative order of elements with equal values is preserved after sorting.
# In-Place: Yes
# Online: Yes
# Adaptable: Yes
# Randomized: No