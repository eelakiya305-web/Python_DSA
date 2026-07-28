class Solution:
    def isanagram(self,word1,word2):
        if sorted(word1)==sorted(word2):
            print("Is Anagram")
        else:
            print("Not an anagram")
    
word1=input("enter word1:").lower()
word2=input("enter word2:").lower()
ob=Solution()
ob.isanagram(word1,word2)
