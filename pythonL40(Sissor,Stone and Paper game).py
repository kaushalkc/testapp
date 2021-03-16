#scissor, Rock and paper game
import random
drawCount=winCount=loseCount=0
i=1
life=int(input("How many life do you want to play.\n"))
print("YOU VS COMPUTER\nLet's see who will win the game\n")
while(i<=life):
    gameList={"s":"scissor","r":"rock","p":"paper"}
    myValue=input("enter your choice\ns ---> scissor\nr ---> rock\np ---> paper\n")
    computerValue = random.choice(list(gameList.keys()))
    print(f"computer choice: \n{computerValue}")
    if computerValue==myValue:
        print(f"Draw game!!!\n{i} life gone.\n{life-i} life left.\n")
        drawCount+=1
    elif (computerValue=='s' and myValue=='p') or (computerValue=='p' and myValue=='r') or (computerValue=='r' and myValue=='s'):
        print(f"Computer won.\n{i} life gone.\n{life-i} life left.\n")
        loseCount+=1
    elif (computerValue=='s' and myValue=='r') or (computerValue=='p' and myValue=='s') or (computerValue=='r' and myValue=='p'):
        print(f"You won.\n{i} life gone.\n{life-i} life left.\n\n")
        winCount+=1
    i+=1
if winCount>loseCount:
    print(f"{drawCount} draw\t {winCount} you won\t {loseCount} computer won\n")
    print("Congratulation you won the game!!!")
elif loseCount>winCount:
    print(f"{drawCount} draw\t {winCount} you won\t {loseCount} computer won\n")
    print("Sorry you lost the game.\nPlay again from start if you like.")
elif winCount==loseCount:
    print(f"{drawCount} draw\t {winCount} you won\t {loseCount} computer won\n")
    print("Game is draw.")
input()

