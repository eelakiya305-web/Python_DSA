class Solution:
    def whichWeekDay(self, day):
        if day==1:
            print("Monday")
        elif day==2:
            print("Tuesday")
        elif day==3:
            print("Wednesday")
        elif day==4:
            print("Thursday")
        elif day==5:
            print("Fridy")
        elif day==6:
            print("Saturday")
        elif day==7:
            print("Sunday")
        else:
            print("Invalid")
ob=Solution()
ob.whichWeekDay(3)
