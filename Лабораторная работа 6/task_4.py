import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    list_ = []
    with open(filename) as f:
        for index, line in enumerate(f):
            fields = line.strip(new_line).split(delimiter)
            if index == 0:
                heads = fields
                continue

            list_.append({})
            for j, _ in enumerate(heads):
                list_[-1][heads[j]] = fields[j]
    return list_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
