
import json


def read_json(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            res = json.load(f)
    except Exception as e:
        raise ValueError("fail to load json file , since {}".format(e))
    return res