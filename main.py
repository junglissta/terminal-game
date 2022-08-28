import random

def players_count():

    players = int(input('How many players?((2-4) '))
    if players < 2 or players > 4:
        print('Wrong number typed. Try again')
        players_count()
    
    return players

players = players_count()

def name():
    if players == 2:
        player_1 = input('Player 1 name: ')
        player_2 = input('Player 2 name: ')
    elif players == 3:
        player_1 = input('Player 1 name: ')
        player_2 = input('Player 2 name: ')
        player_3 = input('Player 3 name: ')
    elif players == 4:
        player_1 = input('Player 1 name: ')
        player_2 = input('Player 2 name: ')
        player_3 = input('Player 3 name: ')
        player_4 = input('Player 4 name: ')


name()