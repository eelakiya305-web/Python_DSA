word1=input().lower()
word2=input().lower()
if sorted(word1)==sorted(word2):
    print("Anagram")
else:
    print("Not a Anagram")