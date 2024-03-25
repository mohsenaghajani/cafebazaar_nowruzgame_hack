import requests
from generate_hash_checksum import get_game_id, generate_checksum
from header import generate_header

data = {
        "checksum": "c9b6a5d91c5193862dab8245f727bea4",
        "date": 1711196085412,
        "gameInstanceId": "",
        "score": 772021
}


def main():
    while True:
        game_id, game = get_game_id(header)
        check_sum = generate_checksum(game, header)
        data['gameInstanceId'] = game_id
        data['checksum'], data['score'], data['date'] = check_sum
        send_score = requests.post(f'https://api.nowruz1403.laeebcup.com/game/score?gameId={game}',
                                   headers=header, json=data)
        result = send_score.json()
        print(result)
        user_choice = input('do you want another ?(y/n)')
        while True:
            if user_choice in ['y', 'n']:
                if user_choice == 'y':
                    break
                else:
                    return
            else:
                print('input invalid try again')
                break


if __name__ == '__main__':
    header = generate_header()
    main()
