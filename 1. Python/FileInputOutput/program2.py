def game():
    return 1000

score = game()
with open("FileInputOutput/score.txt","r") as f:
    highscore=int(f.read())

if highscore<score:
    with open("FileInputOutput/score.txt","w") as f:
        f.write(str(score))


