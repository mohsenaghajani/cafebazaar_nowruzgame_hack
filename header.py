from get_access_token import login

header = {
        'Origin': 'https://nowruz.cafebazaar.app',
        'host': 'api.nowruz1403.laeebcup.com',
        'authority': 'api.digikala.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
                  'avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2NWZmM2QxNGI4ZWJkZTA1ZWUzOTViYzUiLCJpYXQiOjE3MTEyMjYxNTIsImV4cCI6MTcxMTIyNzM1Mn0.ELOzgMZ61EemM2diSF17uC8Q6AeKrJXq44rPZRmbUQk'

}


def generate_header():
    token = login()
    header['Authorization'] = f'Bearer {token}'
    return header
