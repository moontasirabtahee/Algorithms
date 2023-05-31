# Created by Moontasir Abtahee at 5/19/2023
# A simple implementation of insertion Sort Algorithm
# A LIST  have two parts: sorted and unsorted
# we take one element from unsorted part and insert it into sorted part

def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp

    return arr


arr = [7,68,11,62,.2,226,35,0,35,-25,-22,45,-100]
print(insertionSort(arr))