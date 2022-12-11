import re
import json
import os
game_data_path = os.getcwd() + '\\game_data'

def get_intent_command(command):
    re_patterns = {}
    with open(f'{game_data_path}\\command_patterns.json', 'r') as p:
        patterns = json.load(p)
        for intent, pattern in patterns.items():
            re_patterns[intent] = pattern

    intent = None
    entities = []

    for possible_intent, pattern in re_patterns.items():
        match = re.search(pattern, command)
        if match:
            intent = possible_intent
            for i in match.groups():
                entities.append(i)
            break

    return intent, entities
