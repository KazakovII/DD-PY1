import random


def get_random_password() -> str:
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.sample(alpha, 8))


print(get_random_password())
