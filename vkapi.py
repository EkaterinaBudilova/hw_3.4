from urllib.parse import urlencode

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
print(token)

SOURCE_UID = input('Введите ID пользователя: ')
TARGET_UID = input('Введите ID пользователя: ')
ACCESS_TOKEN = input('Введите ACCESS_TOKEN пользователя: ')
FRIENDS_LIST = 'https://api.vk.com/method/friends.get?user_id=307676802&v=5.69'
print(FRIENDS_LIST)
NEW_URL = 'https://api.vk.com/method/friends.getMutual?source_uid={}&target_uid={}&access_token={}&v=5.69'.format(
    SOURCE_UID, TARGET_UID, ACCESS_TOKEN)
print(NEW_URL)