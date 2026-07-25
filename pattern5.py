class Solution:
    def pattern(self,n):
        for i in range(n):
            for j in range(i,n):
                print("*",end="")
            print()
ob=Solution()
ob.pattern(5)