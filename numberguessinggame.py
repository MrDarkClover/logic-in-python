import random as rd

gaming_name=input("Enter you gaming name: ")

computer_choose_num=rd.randint(1,100)
# print(computer_choose_num)

guess=0
player_choose_number=0
while computer_choose_num != player_choose_number:
    player_choose_number=int(input("Enter the number to guess the computer number: "))
    guess+=1

    if player_choose_number < 1 or player_choose_number > 100:
        print("wrong input")
        continue


    if player_choose_number > computer_choose_num:
        print("higher than actual computer num")
    elif computer_choose_num > player_choose_number:
        print("smaller than actual computer num")

print(f"{gaming_name} guessed it correct in {guess} guess")

