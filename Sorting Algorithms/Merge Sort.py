# Created by Moontasir Abtahee at 5/19/2023
# A simple implementation of merge Sort Algorithm
# Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

def mergeSort(arr):
    if len(arr)<1:
        return arr
    mid = len(arr)//2
    p = arr[:mid]
    q = arr[mid:]
    if len(p)>1:
        mergeSort(p)
    if len(q)>1:
        mergeSort(q)

    merge(arr,p,q)


def merge(arr,p,q):
    i = j = k = 0
    result = []
    while i<len(p) and j<len(q):
        if p[i]<q[j]:
            arr[k] = p[i]
            i+=1
        else:
            arr[k] = q[j]
            j+=1
        k+=1

    while i<len(p):
        arr[k] = p[i]
        i+=1
        k+=1

    while j<len(q):
        arr[k] = q[j]
        j+=1
        k+=1

arr = [7,68,11,62,.2,226,35,0,35,-25,-22,45,-100]
mergeSort(arr)
print(arr)