#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    MK = next(iter(a_dictionary))
    MV = a_dictionary[MK]

    for key, value in a_dictionary.items():
        if value > MV:
            MK = key
            MV = value

    return MK
