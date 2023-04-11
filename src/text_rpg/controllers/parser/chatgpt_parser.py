from chatgpt_wrapper import ChatGPT
import json
import controllers.world_controller.player_functions as player_functions

initial_prompt = """Act as though you are an intent parser for a text based adventure game. 
I will enter information for the room that the player is an and then a prompt from the user and you will respond with valid JSON that contains the correct intent from the following list: 
move
equip
unequip
enter
leave
look_around
look_at
pick_up
take
drop
put
eat
use
talk
fight
output_player
quit (used for quitting the game)
invalid_prompt

each of these also has an abbreviation that the user can enter:
m
eq
ue
en
lv
l (on it's own means look_around)
l (with another word, means look_at)
pu
t <object> f? <container>
d
p
e
u
t
f
op
(exit has no abbreviation)

the entities might also be abreiviated. "n" moght stand for north, and so on. make your best guess at what they are supposed to be.

your response should look like:
{
    "intent": <intent>,
    "entities": [<list of relevant entities>]
}

be sure to respond with only one of those intents, names of relevant entities, and nothing else. 
Be as accurate as you can, and if there is an entity that does not make sense, try to figure out what is should be. 
If you understand, simply respond with, "Ok, got it". After that, respond with ONLY JSON unless specifically told to answer something else. 

Examples:

input: enter blacksmith
output:
{
    "intent": "enter",
    "entities": ["blacksmith"]
}

input: talk to jimmy
output:
{
    "intent": "talk",
    "entities": ["jimmy the apple man"]
}

input: enter blacksmith
output:
{
    "intent": "enter",
    "entities": ["blacksmith"]
}

input: eat apple
output:
{
    "intent": "eat",
    "entities": ["apple"]
}

input: look around
output:
{
    "intent": "look_around",
    "entities": []
}

input: glafglart key
output:
{
    "intent": "invalid_prompt",
    "entities": []
}

input: take sword from display rack
output:
{
    "intent": "take",
    "entities": ["sword", "display rack"]
}


"""

bot = ChatGPT()
bot.ask(initial_prompt)

def get_intent_command(command, player, world):
    response = bot.ask(f"room information: {player_functions.look_around(player, world)[1]}\nCommand: {command}")
    d = json.loads(response)
    return d['intent'], d['entities']
