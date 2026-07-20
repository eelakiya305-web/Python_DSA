class Solution:
    def ispalindrome(self,n):
        original=n
        rev=0
        while(n>0):
            digit=n%10
            rev=rev*10+digit
            n=n//10
        return original==rev
n=int(input())
ob=Solution()
print(ob.ispalindrome(n))