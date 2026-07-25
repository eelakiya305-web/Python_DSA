class Solution:
    def pattern(self,n):
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()
ob=Solution()
ob.pattern(5)