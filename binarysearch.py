class Solution:
    def bsearch(self,arr,key):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if key==arr[mid]:
                return mid
            elif key<arr[mid]:
                high=mid-1
            else:
                low=mid+1
arr=list(map(int,input().split()))
key=int(input())
ob=Solution()
print(ob.bsearch(arr,key))