def get_count_char(str_):
    dictionary = {}
    for sym in str_:
        s = sym.lower()
        if sym.isalpha():
            if dictionary.get(s) is not None:
                dictionary.update({s: dictionary.get(s) + 1})
            else:
                dictionary[s] = 1
    return dictionary


def get_percent_char(dict_):
    dictionary = {}
    total_chars = 0

    for keys in dict_:
        total_chars += dict_.get(keys)

    for keys in dict_:
        dictionary.update({keys: (dict_.get(keys) / total_chars * 100).__round__(2)})

    return dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
