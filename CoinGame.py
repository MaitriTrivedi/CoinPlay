import random
while 1:
    print('1. TO PLAY')
    print('2. TO EXIT')
    print('3. TO KNOW WINNER')
    ch=int(input("Enter Your Choice :"))
    if ch==2:
        break
    player1=input("Enter Player One Name :")
    player2=input("Enter Player Two Name :")
    score1=0
    score2=0
    round=int(input('How many rounds do you want to play? '))
    for i in range(1,round+1):
        randmCoin=random.choice('HT')
        if i%2==0 :
            choice=input("Player2, Enter Your Choice :")
            if choice==randmCoin:
                score2+=10
        else :
            choice=input("Player1, Enter Your Choice :")
            if choice==randmCoin:
                score1+=10
    if score1>score2:
        print("PLAYER1 IS THE WINNER.")
    elif score1<score2:
        print("PLAYER2 IS THE WINNER.")
    else:
        print("IT IS TIE")
    print("PLAYER1 : "+str(score1)+"\n"+"PLAYER2 : "+str(score2))
    
