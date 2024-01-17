import requests
from bot.bot_config import Settings
from bot.bot_utils import *


get_token = requests.get(set_url('register'))
registered_users = []

for user in range(Settings.number_of_users):
    password = string_generator()
    registration_data = {
        'csrfmiddlewaretoken': get_token.cookies.get('csrftoken'),
        'username': string_generator(),
        'password1': password,
        'password2': password,
        'email': generate_random_email(),
    }
    response = requests.post(set_url('register'), data=registration_data, cookies=get_token.cookies)
    registered_users.append(registration_data)

for user in registered_users:
    login_data = {"username": user['username'], "password": user['password1']}
    tokens = requests.post(set_url('api/token/'), data=login_data, cookies=get_token.cookies)
    headers = {"Authorization": "Bearer " + tokens.json()['access']}

    for post in range(Settings.max_posts_per_user):
        post_data = {
            "title": string_generator(),
            "body": string_generator(20)
        }
        requests.post(set_url('api/post/'), data=post_data, headers=headers, cookies=get_token.cookies)

for user in registered_users:
    login_data = {"username": user['username'], "password": user['password1']}
    tokens = requests.post(set_url('api/token/'), data=login_data, cookies=get_token.cookies)
    headers = {"Authorization": "Bearer " + tokens.json()['access']}

    posts = requests.get(set_url('api/post/'), headers=headers, cookies=get_token.cookies)
    rand_posts = random_elements_from_list(posts.json()['results'])

    for post in rand_posts:
        requests.post(set_url(f'api/post/{post["id"]}/like/'), headers=headers, cookies=get_token.cookies)

