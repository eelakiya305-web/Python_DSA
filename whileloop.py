class Solution:
    def whileLoop(self,d:int)->int:
        sum=0
        count=0
        if d==0:
            d=10
        while(count<50):
            sum+=d
            d+=10
            count+=1
        return sum
ob=Solution()
print(ob.whileLoop(2))
