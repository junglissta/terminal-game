import random

card_deck = '2222444455556666777788889999'
card_deck_list = list(card_deck)
for i in range(4):
    card_deck_list.append('10')


p1 = []
p2 = []
p3 = []
p4 = []
players = 2
def players_count():

    players = int(input('How many players?((2-4) '))
    if players < 2 or players > 4:
        print('Wrong number typed. Try again')
        players_count()
    
    return players

players = players_count()


if players == 2:
    player_1 = input('Player 1 name: ')
    player_2 = input('Player 2 name: ')
    print('Hello players. Welcome to this small terminal game. Its a card game where each player gets random card and higher value wins. player with most cards at the end wins million euro :D')
elif players == 3:
    player_1 = input('Player 1 name: ')
    player_2 = input('Player 2 name: ')
    player_3 = input('Player 3 name: ')
    print('Hello players. Welcome to this small terminal game. Its a card game where each player gets random card and higher value wins. player with most cards at the end wins million euro :D')
elif players == 4:
    player_1 = input('Player 1 name: ')
    player_2 = input('Player 2 name: ')
    player_3 = input('Player 3 name: ')
    player_4 = input('Player 4 name: ')
    print('Hello players. Welcome to this small terminal game. Its a card game where each player gets random card and higher value wins. player with most cards at the end wins million euro :D')
input('Press enter to continue')


def game_on():
    if players == 2:
        for i in range(len(card_deck_list)//2 - 1):
            play_1 = random.choice(card_deck_list)
            play_2 = random.choice(card_deck_list)
        
            card_deck_list.remove(play_1)
            card_deck_list.remove(play_2)
            if int(play_1) > int(play_2):
                p1.append(play_1)
                p1.append(play_2)
                print(p1)
                print(p2)
                print('Player1 wins this round')
            else:
                p2.append(play_1)
                p2.append(play_2)
                print(p2)
                print(p1)
                print('Player2 wins this round')
            input('press any key to continue')
        if len(p1) > len(p2):
            print('player1 wins')
         
        else:
            print('player2 wins')
    elif players == 3:
        for i in range(len(card_deck_list)//3):
            play_1 = random.choice(card_deck_list)
            play_2 = random.choice(card_deck_list)
            play_3 = random.choice(card_deck_list)
        
            card_deck_list.remove(play_1)
            card_deck_list.remove(play_2)
            card_deck_list.remove(play_3)
            
            if int(play_1) > int(play_2) and int(play_1) > int(play_3):
                p1.append(play_1)
                p1.append(play_2)
                p1.append(play_3)
                print(p1)
                print(p2)
                print(p3)
                print(f'{player_1} wins this round')
            elif int(play_2) > int(play_1) and int(play_2) > int(play_3):
                p2.append(play_1)
                p2.append(play_2)
                p2.append(play_3)
                print(p2)
                print(p1)
                print(p3)
                print(f'{player_2} wins this round')
            else:
                p3.append(play_1)
                p3.append(play_2)
                p3.append(play_3)
                print(p3)
                print(p2)
                print(p1)
                print(f'{player_3} wins this round')
            input('press enter to continue')
        if len(p1) > len(p2) and len(p1) > len(p3):
            print(f'{player_1} wins')
        elif len(p2) > len(p1) and len(p2) > len(p3):
            print(f'{player_2} wins')
        else:
            print(f'{player_3} wins')
    else:
        for i in range(len(card_deck_list)//4):
            play_1 = random.choice(card_deck_list)
            play_2 = random.choice(card_deck_list)
            play_3 = random.choice(card_deck_list)
            play_4 = random.choice(card_deck_list)
        
            card_deck_list.remove(play_1)
            card_deck_list.remove(play_2)
            card_deck_list.remove(play_3)
            card_deck_list.remove(play_4)
            
            if int(play_1) > int(play_2) and int(play_1) > int(play_3) and int(play_1) > int(play_4):
                p1.append(play_1)
                p1.append(play_2)
                p1.append(play_3)
                p1.append(play_4)
                print(player_1 + p1)
                print(player_2 + p2)
                print(player_3 + p3)
                print(player_4 + p4)
                print(f'{player_1} wins this round')
            elif int(play_2) > int(play_1) and int(play_2) > int(play_3) and int(play_2) > int(play_4):
                p2.append(play_1)
                p2.append(play_2)
                p2.append(play_3)
                p2.append(play_4)
                print(player_2 + p2)
                print(player_1 + p1)
                print(player_3 + p3)
                print(player_4 + p4)
                print(f'{player_2} wins this round')
            elif int(play_3) > int(play_1) and int(play_3) > int(play_2) and int(play_3) > int(play_4):
                p3.append(play_1)
                p3.append(play_2)
                p3.append(play_3)
                p3.append(play_4)
                print(player_3 + p3)
                print(player_2 + p2)
                print(player_1 + p1)
                print(player_4 + p4)
                print(f'{player_3} wins this round')
            else:
                p4.append(play_1)
                p4.append(play_2)
                p4.append(play_3)
                p4.append(play_4)
                print(player_4 + p4)
                print(player_2 + p2)
                print(player_1 + p1)
                print(player_3 + p3)
                print(f'{player_4} wins this round')
            input('press enter to continue')
        if len(p1) > len(p2) and len(p1) > len(p3) and len(p1) > len(p4):
            print(f'{player_1} wins')
        elif len(p2) > len(p1) and len(p2) > len(p3) and len(p2) > len(p4):
            print(f'{player_2} wins')
        elif len(p3) > len(p1) and len(p3) > len(p2) and len(p3) > len(p1):
            print(f'{player_3} wins')
        else:
            print(f'{player_4} wins')

game_on()

