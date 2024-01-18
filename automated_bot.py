import requests
from bot.config import Settings
from bot.utils import *


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
    response = register_user(registration_data, get_token.cookies)
    registered_users.append(registration_data)

for user in registered_users:
    login_data = {"username": user['username'], "password": user['password1']}
    headers = login(login_data, get_token.cookies)

    for post in range(Settings.max_posts_per_user):
        post_data = {
            "title": string_generator(),
            "body": string_generator(20)
        }
        create_post(post_data, headers, get_token.cookies)

for user in registered_users:
    login_data = {"username": user['username'], "password": user['password1']}
    headers = login(login_data, get_token.cookies)
    posts = get_posts(headers, get_token.cookies)
    rand_posts = random_elements_from_list(posts.json()['results'])

    for post in rand_posts:
        like_post(post["id"], headers, get_token.cookies)
