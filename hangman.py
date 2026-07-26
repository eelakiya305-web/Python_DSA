word="python"
guessed=[]
chances=6
while chances>0:
    display=""
    for letter in word:
        if letter in guessed:
            display+=letter+""
        else:
            display+="_"
    print(display)
    if "_" not in display:
        print("you won!")
        break
    guess=input().lower()
    if guess in word:
        guessed.append(guess)
    else:
        choices-=1
        print("wrong guess")
        print(chances)
    if chances==0:
        print("you lost")
        print(word)
        
