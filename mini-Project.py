import random

print("************************Hi****************************")
print("**********Welcome to Rock-Paper-scissor game**********")
no_game=int(input("Enter the number of games you want to play : "))
count=1
user_count=0
computer_count=0

for i in range(no_game):
    user_in=str(input("Enter the your option to play the game your options are #rock #papaer #scissor : "))
           
    if user_in in ["rock" ,"paper" ,"scissor"]:
            
        option =["rock" ,"paper" ,"scissor"]
        computer_in=(random.choice(option))
        if len(user_in) == len(computer_in):
                print("Tie")
        elif len(user_in) > len(computer_in):
                print("Win")
                user_count = user_count + 1
        elif len(user_in) < len(computer_in):
                print("Lose")
                computer_count = computer_count + 1
        
        
    else:
            
                  print("Kindly enter valid input")
                  print("your inputs can be one of the below")
                  print("rock")
                  print("paper")
                  print("scissor")
                  
                  if count < 5:
                      count = count+1
                      print(count)
                  else:
                      print("***************Sry try to enjoy the game with rules next time....***************")
                      break
                        
                                               
if user_count > computer_count:
    print("Number of games played:",no_game)
    print("Number of games you have won:",user_count)
    print("Number of games computer has won:",computer_count)
    print("***************Congrats!!!! you have won.....***************")
    print("-----you have won the match-----")
elif user_count < computer_count:
    print("Number of games played:",no_game)
    print("Number of games you have won:",user_count)
    print("Number of games computer has won:",computer_count)
    print("***************   Sry :-)....have a luck next time   ***************")
    print("-------------------------computer have won the match-------------------------")
elif user_count == 0 and computer_count == 0:
    print("***************   Sry try to enjoy the game with rules next time....***************")
elif user_count == computer_count:
    print("Number of games played:",no_game)
    print("Number of games you have won:",user_count)
    print("Number of games computer has won:",computer_count)
    print("******************************   Sry :-)....It was a tie   ******************************")
    print("-------------------------Win was shared between you and computer-------------------------")
    
    
