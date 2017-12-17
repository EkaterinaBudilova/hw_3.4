from urllib.parse import urlencode
import requests

def get_token():
    AUTH_URL = 'http://oauth.vk.com/authorize'
    APP_ID = 6287762

    url_data = {
        'client_id': APP_ID,
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'display': 'page',
        'scope': 'friends',
        'response_type': 'token',
        'v': '5.69'
    }

    token = '?'.join(
        (AUTH_URL, urlencode(url_data)
         ))
    return token

def mutual_friends():
    source_uid = input('Введите ID пользователя: ')
    target_uid = input('Введите ID пользователя: ')
    access_token = input('Введите ACCESS_TOKEN пользователя: ')
    new_url = 'https://api.vk.com/method/friends.getMutual?source_uid={}&target_uid={}&access_token={}&fields=nickname&v=5.69'.format(
        source_uid, target_uid, access_token)
    text = requests.get(url = new_url).json()
    return text['response']

if __name__ == '__main__':
    token_url = get_token()
    print(token_url)
    friends_list = mutual_friends()
    for frand_id in friends_list:
        print(frand_id, 'http://vk.com/id' + str(frand_id))