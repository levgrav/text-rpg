import re
import json
import os
game_data_path = 'files/game_data'

def get_intent_command_standard(command, *_):
    re_patterns = {}
    with open(f'files/game_data/command_patterns.json', 'r') as p:
        patterns = json.load(p)
        for intent, pattern in patterns.items():
            re_patterns[intent] = pattern

    intent = "invalid_prompt"
    entities = []

    for possible_intent, pattern in re_patterns.items():
        match = re.search(pattern, command)
        if match:
            intent = possible_intent
            for i in match.groups():
                entities.append(i)
            break

    return intent, entities


get_intent_command = get_intent_command_standard

def set_parser(parser_type):
    global get_intent_command
    match parser_type:
        case 'gpt':
            import controllers.parser.chatgpt_parser as gpt
            get_intent_command = gpt.get_intent_command
        case 'standard':
            get_intent_command = get_intent_command_standard



