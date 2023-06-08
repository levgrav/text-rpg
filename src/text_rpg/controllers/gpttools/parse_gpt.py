import json
import controllers.world_controller.player_functions as player_functions
import openai

with open('files/game_data/settings.json') as f:
    openai.api_key_path = json.load(f)['openai_api_key_path']

messages = [
    {
        "role": "system",
        "content": """You are a parser. Your job is to write JSON for a text-adventure game that is a parsed version of a user's message. The JSON should contain the following fields: 'command', 'args'. The user may have typos and they may use chortcuts, so do your best to interperet what they are saying. Remember, respond in only JSON.
Here is a list of all commands that the user may use: 'move', 'equip', 'unequip', 'enter', 'leave', 'look_around', 'examine', 'pick_up', 'take', 'drop', 'put', 'eat', 'use', 'talk', 'fight', 'output_player', 'quit' (used for quitting the game), 'invalid_prompt'
each of these also has an abbreviation that the user can enter:
'm', 'eq', 'ue', 'en', 'lv', 'l', 'ex', 'pu', 't <object> f? <container>', 'd', 'p', 'e', 'u', 't', 'f', 'op', (quit has no abbreviation)""",
    },
    {
        "role": "user",
        "content": "move north",
    },
    {"role": "assistant", "content": '{"command": "move", "args": ["north"]}'},
    {
        "role": "user",
        "content": "talk to the wizard",
    },
    {"role": "assistant", "content": '{"command": "talk", "args": ["wizard"]}'},
    {
        "role": "user",
        "content": "figt the goblinn",
    },
    {"role": "assistant", "content": '{"command": "fight", "args": ["goblin"]}'},
]

def get_intent_command(command, player, world):
    messages.append({"role":"system", "content": f"Specific room information: {player_functions.look_around(player, world)[1]}\n All entities that the user may interact with will be here"})
    messages.append({"role": "user", "content": command})
    
    for i in range(3):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            break
        except Exception as e:
            print("Error: ", e)
    else:
        print("Failed to get response from OpenAI API")
        return "error", []
    
    messages.pop()  # remove the user's message
    messages.pop()  # remove the system's message
    content = response.choices[0]["message"]["content"] # type: ignore
    content_dict = json.loads(content)
    
    try:
        return content_dict['command'], content_dict['args']
    except KeyError:
        print("Error: ", content_dict)
        return "error", []

