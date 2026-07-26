import random
doors=[1,2,3]
prize=random.choice(doors)
choice=int(input())
host=[d for d in doors if d!=choice and d!=prize][0]
print(host)
switch=input().lower()
if(switch=="yes"):
    print("Congratulations!")
else:
    print("Sorry")