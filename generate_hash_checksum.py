import requests
import time
import hashlib


def generate_checksum(game, header):
    date = int(time.time() * 1000)
    get_user_score = int(input('enter score :'))
    uid = get_uid(header)
    salt = 'nowruz1403salt'
    sum_item = f'{get_user_score}:{date}:{game}:{uid}:{salt}'
    hash = (hashlib.md5(f'{sum_item}'.encode('utf-8')).hexdigest())
    return hash, get_user_score, date


def get_game_id(header):
    game = choice_game()
    url = f'https://api.nowruz1403.laeebcup.com/game/game-instance?gameId={game}'
    response = requests.get(url, headers=header)
    data = response.json()
    try:
        game_id = data['data']['gameInstanceId']
        return game_id, game
    except:
        print(data)


def choice_game():
    while True:
        user_choice = int(input('which game do you want to hack score ? 1.pocket soccer 2.karate 3.protect me :'))
        if user_choice in [1, 2, 3]:
            if user_choice == 1:
                return 'pocket-world-cup'
            elif user_choice == 2:
                return 'karate-kido-2'
            elif user_choice == 3:
                return 'protect-me'
        else:
            print('input is invalid try again')


def get_uid(header):
    url = 'https://api.nowruz1403.laeebcup.com/user/profile'
    response = requests.get(url, headers=header)
    data = response.json()
    return data['data']['uid']