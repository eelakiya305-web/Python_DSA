class Solution:
    def InsertionSort(self,arr):
        n=len(arr)
        for i in range(n):
            key=arr[i]
            j=i-1
            while j>0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr
arr=list(map(int,input().split()))
ob=Solution()
print(ob.InsertionSort(arr))
