import string
import random


def string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_random_email():
    domains = ['gmail.com', 'yahoo.com']
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(domains)
    return f'{username}@{domain}'


def set_url(additional: str):
    return "http://127.0.0.1:8000/star-navi/" + additional


def random_elements_from_list(my_list):
    num_elements = random.randint(1, len(my_list))
    random_elements = random.sample(my_list, num_elements)
    return random_elements
