class Solution:
    def gcd(self,a,b):
        while(b!=0):
            a,b=b,a%b
        return a
ob=Solution()
print(ob.gcd(104,356))