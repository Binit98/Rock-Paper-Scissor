def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print ("DRAW")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print ("Player 1 choosed ROCK & Player 2 choosed SCISSOR,Player 1 won!!")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print ("Player 1 chossed ROCK & Player 2 choosed PAPER,Player 2 won!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
        print ("Player 1 choosed PAPER & Player 2 choosed SCISSOR,Player 2 won!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print ("Player 1 choosed PAPER & Player 2 choosed ROCK,Player 1 won!!")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print ("Player 1 choosed SCISSOR & Player 2 choosed PAPER,Player 1 won!!")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print ("Player 1 choosed SCISSOR & Player 2 choosed ROCK,Player 2 won!!")

player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',2:'Rock',3:'Scissor'}
while(1):
    num1=input("Player one,Enter your choice")
    num2=input("Player two,Enter your choice")
    bit1=int(input("Player one,Enter your secret bit"))
    bit2=int(input("Player two,Enter your secret bit"))
    rock_paper_scissor(num1,num2,bit1,bit2)
   
