import requests
from generate_hash_checksum import get_game_id, generate_checksum
import time
from header import headers
from check_leader_score import check_scores
from concurrent.futures import ThreadPoolExecutor
data = {
        "checksum": "c9b6a5d91c5193862dab8245f727bea4",
        "date": 1711196085412,
        "gameInstanceId": "",
        "score": 772021
}


def main(header, game, user, refresh):
    while True:
        score = check_scores(user, game)
        if score:
            game_id, game = get_game_id(header, game, refresh)
            check_sum = generate_checksum(game, header, score)
            data['gameInstanceId'] = game_id
            data['checksum'], data['score'], data['date'] = check_sum
            send_score = requests.post(f'https://api.nowruz1403.laeebcup.com/game/score?gameId={game}',
                                       headers=header, json=data)
            result = send_score.json()
            print(result, 'n')
        else:
            print(f'we are won in {game} ')
        time.sleep(5)


def thread():
    executor = ThreadPoolExecutor(max_workers=15)
    try:
        for header in headers:
            executor.submit(main, header['header'], header['game'], header['user'], header['refresh'])
    except:
        print('we have problem in thread')
    executor.shutdown()


def refresh_token(token):
    header = headers[0]['header']
    data = {
        "refreshToken": f"{token}"
    }
    url = 'https://api.nowruz1403.laeebcup.com/auth/refresh-token'
    response = requests.post(url, headers=header, json=data)
    d = response.json()
    print(d)


if __name__ == '__main__':
    thread()
