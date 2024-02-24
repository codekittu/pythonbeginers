#Display a list ., let user choose a index position and value and replace it




def display_game(game_list):
    print('Here is the game list: ')
    print(game_list)



def position_choice():
    choice ='wrong'

    while choice not in ['0','1','2']:

        choice = input("pick a position (0,1,2): ")

        if choice not in ['0','1','2']:
            print("Invalid choice !!")

    return int(choice)



def replacement_choice(game_list,postion):

    user_placement = input("Give a string, positon: ")
    game_list[postion] = user_placement
    return game_list




def gameon_choice():
    choice ='wrong'

    while choice not in ['Y','N']:

        choice = input("Keep playing (Y or N): ")

        if choice not in ['Y','N']:
            print("Unacceptable input, choose Y or N !!")

    if choice =='Y':
        return True
    else:
        return False

game_on=True
game_list =[0,1,2]

while game_on == True:
    display_game(game_list)
    position =position_choice()
    game_list= replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()
