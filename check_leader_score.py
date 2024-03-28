import requests
import random


def check_scores(user, game):
    url = f'https://api.nowruz1403.laeebcup.com/game/leaderboard?gameId={game}'
    response = requests.get(url)
    data = response.json()
    leader = data['data'][0]['user']['username']
    leader_score = data['data'][0]['score']

    if leader != user:
        score = leader_score + random.randint(1, 10)
        return score
    return False


