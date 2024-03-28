import requests


def get_client_id():
    while True:
        get_phone_number = input('enter your phone number :')
        data = {
            "phone": f"{get_phone_number}"
        }
        url = 'https://api.nowruz1403.laeebcup.com/auth/login'
        response = requests.post(url, json=data)
        response_data = response.json()
        if response.status_code == 200 :
            date_response = response.json()
            client_id = date_response['data']['clientId']
            return client_id
        else:
            if response_data['message'] == "user does not exist!":
                return sign_in()
            else:
                print('phone number is invalid try again ')


def login():
    client_id = get_client_id()
    url = 'https://api.nowruz1403.laeebcup.com/auth/verify'
    while True:
        get_code = input('enter code :')
        data = {"clientId": f"{client_id}",
                "pinCode": f"{get_code}"}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            response_data = response.json()
            token = response_data['data']['accessToken']
            return token
        else:
            print('code is invalid try again')


def sign_in():
    while True:
        get_username = input('enter username :')
        phone_number = input('enter phone number')
        data = {"phone": f"{phone_number}", "username": f"{get_username}"}
        url = 'https://api.nowruz1403.laeebcup.com/auth/register'
        response = requests.post(url, json=data)
        if response.status_code == 200:
            date_response = response.json()
            client_id = date_response['data']['clientId']
            return client_id
        else:
            print('username is invalid try again ')