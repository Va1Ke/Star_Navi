import string
import random
import requests
from bot.config import Settings


def string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_random_email():
    domains = ['gmail.com', 'yahoo.com']
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(domains)
    return f'{username}@{domain}'


def random_elements_from_list(my_list: list):
    num_elements = random.randint(1, len(my_list))
    random_elements = random.sample(my_list, num_elements)
    return random_elements


def set_url(additional: str):
    return Settings.base_url + additional


def login(data: dict, cookies):
    tokens = requests.post(set_url('api/token/'), data=data, cookies=cookies)
    return {"Authorization": "Bearer " + tokens.json()['access']}


def register_user(data: dict, cookies):
    return requests.post(set_url('register'), data=data, cookies=cookies)


def create_post(data: dict, headers: dict, cookies):
    return requests.post(set_url('api/post/'), data=data, headers=headers, cookies=cookies)


def get_posts(headers: dict, cookies):
    return requests.get(set_url('api/post/'), headers=headers, cookies=cookies)


def like_post(post_id: int, headers: dict, cookies):
    return requests.post(set_url(f'api/post/{post_id}/like/'), headers=headers, cookies=cookies)
