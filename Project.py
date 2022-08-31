import random
import requests

def random_pokemon ():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
#        'hp': pokemon['hp'],
#        'attack': pokemon['attack'],
#        'defense': pokemon['defense'],
#        'speed': pokemon['speed'],
#        'special_attack': pokemon['sp_atk'],
#        'special_defense': pokemon['sp_def'],
    }
def run ():
    print("~~ Welcome to the Pokemon Top Trumps Game! ~~ \n")
    playerOneName = input("Player 1, please enter your name: ")
    print("Hello " + playerOneName + ", get ready to enter the world of Pokemon!\n")
    computerName = "Ash"
    print("You are playing against " + computerName + ", get ready...\n")

    my_Pokemon = random_pokemon()
    opponent_Pokemon = random_pokemon()

    print('{} was given {}'.format(playerOneName, my_Pokemon['name']))
    statChoice = input('Which stat do you want to use? (id, height, weight) ')

    myStat = my_Pokemon[statChoice]
    opponentStat = opponent_Pokemon[statChoice]

    print('{} chose {}'.format(computerName, opponent_Pokemon['name']))

    if myStat > opponentStat:
        print('You Win!')
    elif myStat < opponentStat:
        print('You Lose!')
    else:
        print('Draw!')
        my_Pokemon = random_pokemon()
        opponent_Pokemon = random_pokemon()

        print('{} was given {}'.format(playerOneName, my_Pokemon['name']))
        statChoice = input('Which stat do you want to use? (id, height, weight) ')

        myStat = my_Pokemon[statChoice]
        opponentStat = opponent_Pokemon[statChoice]

        print('{} chose {}'.format(computerName, opponent_Pokemon['name']))
        if myStat > opponentStat:
                print('You Win!')
        elif myStat < opponentStat:
                print('You Lose!')
        else:
            print('Draw!')

run()