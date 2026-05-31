import game_art as g
import random as r

print(g.r_p_s_logo)
outcomes=[0,1,2]
computer_choice=r.choice(outcomes)
print("0 for rock\n1 for paper\n2 for scissor ")
choice=int(input("enter your choice"))

#print(computer_choice)

game_image=[g.rock,g.paper,g.scissor]

print(f"your choice{game_image[choice]}")
print(f"computer choice{game_image[computer_choice]}")

if choice==computer_choice:
    print("draw")
elif choice>2 or choice<0:
    print("invalid input\n you lose")   
elif choice==0 and computer_choice==2:
    print("you wins")   
elif choice==2 and computer_choice==0:
    print("computer wins")   
elif computer_choice>choice:
    print("computer wins")     
elif choice>computer_choice:
    print("you wins")  

        
     

     



