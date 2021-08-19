import mgame
score=mgame.guess()
print(f"congratulations u won ...attempts you took is {score}")
with open("hiscore.txt","r") as f:
    hiscore=f.read()
if hiscore=='':
        print("this was a new game...your score is the first highscore")
        with open("hiscore.txt","w")as f:
            f.write(str(score))
elif score>int(hiscore):
    print("u have not set the highscore")
elif score<int(hiscore):
    print("congratulations you have just set a new highscore")
    with open("hiscore.txt","w")as f:
            f.write(str(score))

