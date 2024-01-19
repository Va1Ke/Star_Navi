import requests
from bot.config import Settings
from bot import utils


get_token = requests.get(utils.set_url('register'))
registered_users = []

for user in range(Settings.number_of_users):
    password = utils.string_generator()
    registration_data = {
        'csrfmiddlewaretoken': get_token.cookies.get('csrftoken'),
        'username': utils.string_generator(),
        'password1': password,
        'password2': password,
        'email': utils.generate_random_email(),
    }
    response = utils.register_user(registration_data, get_token.cookies)
    registered_users.append(registration_data)

for user in registered_users:
    login_data = {"username": user['username'], "password": user['password1']}
    headers = utils.login(login_data, get_token.cookies)

    for post in range(Settings.max_posts_per_user):
        post_data = {
            "title": utils.string_generator(),
            "body": utils.string_generator(20)
        }
        utils.create_post(post_data, headers, get_token.cookies)

for user in registered_users:
    login_data = {"username": user['username'], "password": user['password1']}
    headers = utils.login(login_data, get_token.cookies)
    posts = utils.get_posts(headers, get_token.cookies)
    rand_posts = utils.random_elements_from_list(posts.json()['results'])

    for post in rand_posts:
        utils.like_post(post["id"], headers, get_token.cookies)
