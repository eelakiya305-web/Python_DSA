class Solution:
    def flamesfornames(self,name1,name2):

        name1=name1.lower().replace("","")
        name2=name2.lower().replace("","")
        for ch in name1[:]:
            if ch in name2:
                name1=name1.replace(ch,"",1)
                name2=name2.replace(ch,"",1)
                count=len(name1)+len(name2)
                flames=["Freinds","Love","Affection","Marriage","Enemy","Sister"]
                while len(flames)>1:
                    index=(count-1)%len(flames)
                    flames.pop(index)
                    flames=flames[index:]+flames[:index]
                return(flames[0])
name1=input()
name2=input()
ob=Solution()
print(ob.flamesfornames(name1,name2))