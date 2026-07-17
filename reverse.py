class Solution:
    def reverse(self,arr:list)-> None:
        s=0
        e=len(arr)-1
        while(s<e):
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
arr=list(map(int,input().split()))
ob=Solution()
result=ob.reverse(arr)
print(arr)
