import requests
import time
import hashlib


def refresh_token(header, token):
    print('token expired generate new token')
    data = {
        "refreshToken": f"{token}"
    }
    url = 'https://api.nowruz1403.laeebcup.com/auth/refresh-token'
    response = requests.post(url, headers=header, json=data)
    response_data = response.json()
    new_token = response_data['data']["accessToken"]
    print(new_token)
    header['Authorization'] = f'Bearer {new_token}'
    print('new token ')
    return header


def generate_checksum(game, header, score):
    date = int(time.time() * 1000)
    uid = get_uid(header)
    salt = 'nowruz1403salt'
    sum_item = f'{score}:{date}:{game}:{uid}:{salt}'
    hash = (hashlib.md5(f'{sum_item}'.encode('utf-8')).hexdigest())
    return hash, score, date


def get_game_id(header, type_game, refresh):
    while True:
        game = type_game
        url = f'https://api.nowruz1403.laeebcup.com/game/game-instance?gameId={game}'
        response = requests.get(url, headers=header)
        data = response.json()
        if response.status_code != 200:
            if data['message'] == 'accessToken expired!':
                refresh_token(header, refresh)
        else:
            game_id = data['data']['gameInstanceId']
            return game_id, game


def get_uid(header):
    url = 'https://api.nowruz1403.laeebcup.com/user/profile'
    response = requests.get(url, headers=header)
    data = response.json()
    return data['data']['uid']