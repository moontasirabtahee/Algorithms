# Created by Moontasir Abtahee at 5/21/2023
# a simple implementation of shell Sort Algorithm

def shellSort(arr):
    #n = len(arr)  for(gap = n/2;gap>0;gap/=2)
    gap = len(arr)//2
    while gap>0:
        print(gap)
        print(len(arr))
        for i in range(gap,len(arr)):
            j = i -gap
            while j>=0 and arr[j]>arr[j+gap]:
                arr[j],arr[j+gap] = arr[j+gap],arr[j]
                j-=gap
        gap//=2
    return arr


arr = [-25,56,88,0,36,-632,458,-1,696,558,15,5,68]

print(shellSort(arr))