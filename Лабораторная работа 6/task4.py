import json

INPUT_FILE = "input.csv"
# у вас input.csv битый, чтобы решить задачу пришлось чинить файл, подсматривая в решение


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:

    with open(filename, "r") as f:
        list_ = []
        [columns, *values] = f.read().splitlines()
        columns = columns.split(delimiter)

        for string in values:
            string = string.split(delimiter)
            dict_ = {}
            for i in range(len(columns)):
                dict_[columns[i]] = string[i]
            list_.append(dict_)

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
