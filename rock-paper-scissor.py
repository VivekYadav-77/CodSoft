import random
import calheading
print(calheading.logo3)
l = ["rock","paper","scissor"]
h = True
while h is True:
    choice = int(input("enter the 0 for rock , 1 for paper , 2 for scissors :"))
    user_choice = choice
    computer_choice = random.randint(0,2)
    if user_choice<0 or user_choice>2:
        print("enter the valid number")
    elif user_choice == 2 and computer_choice == 0:
        print(f"you lose {l[0]} wins against {l[2]}")
    elif computer_choice == 2 and user_choice == 0:
        print(f"you won {l[2]} won against {l[0]} ")
    elif computer_choice>user_choice:
        print(f"you lose {l[computer_choice]} wins against {l[user_choice]} ")
    elif user_choice>computer_choice:
        print(f"you won {l[user_choice]} wins against {l[computer_choice]}")
    elif user_choice == computer_choice:
        print("draw")
    else:
        print("enter the defined numbers for playing game")
    askuser = input("if you want to play again then write yes otherwise write no : ").lower()
    if askuser == "no":
        h = False