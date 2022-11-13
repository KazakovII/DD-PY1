import random


def get_unique_list_numbers() -> list[int]:
    list_ = [i for i in range(-10, 11)]
    for i in range(6):
        delete_ = (random.random()*(len(list_)-1)).__round__()
        list_.pop(delete_)

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

