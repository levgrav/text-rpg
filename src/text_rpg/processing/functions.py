"""processing.functions
~~~~~~~~~~~~~~~~~~~
File that contains lots of useful functions that are called in a variety of places"""

# --- Imports --- #
import os
from processing.classes import Class

# --- Functions --- #
def explore(obj, def_attr: str = 'name'):
    """Allows the user to 'explore' an object from the console. Is generally used for testing purposes. It is kind of a janky function, but it works.

    Args:
        obj (Any): the object that the user will explore
        def_attr (str, optional): default attribute by which to display all objects. Defaults to 'name'.
    """
    
    os.system('cls') # Clear screen
    
    # Displaying the initial object
    print(obj.__getattribute__(def_attr))
    for attribute in obj.__dict__.keys():
        print(f'  {attribute}')

    # taking user inout
    look_at = input("\nWhich attribute would you like to look at?\n")
    try:
        attribute = obj.__getattribute__(look_at)
    except AttributeError: # if user entered invalid attribute, 'AttributeError' will be displayed
        attribute = 'AttributeError'
    
    print(f"\nType: {type(attribute)}\n") # outputs the type of the requested attribute

    # output depends on the type of object
    if type(attribute) == str:
        print(attribute) #in the case of strings, just printing them out work well.
        
    elif type(attribute) == list:
        if attribute.__len__() == 0: # if the list is empty, that is helpful to know
            print('Empty list')            
        else:
            # allows the user to choose on of the elements in the list, then calls this function on that element.
            try:
                for value in attribute: # prints entire list based on default attribute
                    print(value.__getattribute__(def_attr))
                
                choice = input('\nChoose one of the above: ') # user chooses one of the above displayed values
                
                for value in attribute:
                    if value.__getattribute__(def_attr) == choice:
                        explore(value, def_attr) # calls `explore` on the chosen element
                
                # if the program failed to exit
                print("\nNot found")
            
            except AttributeError:
                # if `def_attr` is not an attribute of a value in the list, all values are printed 
                for value in attribute:
                    print(value)
                """ 
                Ex. list -> [1, 2, 3, "Hello World!"]
                Output: 
                1
                2
                3
                Hello World!
                """
    else: # if object has elements that are neither string nor list, it just ignores them
        print('Unknown Type')

    # after everything is done, the program exits
    input('\nPress <enter> to exit')
    exit()

def disp_obj(obj, def_attr: str = "", indent = 0):
    """Provides a standard way to display an object as text. Attributes are displayed in a list, vertically. 
    

    Args:
        obj (Any): the object that will be displayed
        def_attr (str, optional): default attribute. Used to label objects. Defaults to "".
        indent (int, optional): is used if it is being displayed inside something. indents all lines. Defaults to 0.

    Returns:
        str: a string representation of all the attributes in the object.
            Ex. def_attr = 'name' ("..." used for brevity)
            Bob
                name: Bob
                referrals: []
                species: "Human"
                ...
                inventory: ['sword']
                equipped: 
                    head: None
                    chest: None
                    primary: None
                    ...
                ...
    """
    
    out = '' # initializes output
    
    # if default attrubute is given, object is labeled with it
    if def_attr != '':
        
        if def_attr not in obj.__dict__.keys(): # if bad def_attr is given
            return f"Bad def_attr: '{def_attr}'"
    
        out += indent * "  " + obj.__getattribute__(def_attr)

    # loops through all attributes
    for attribute in obj.__dict__.keys():
        out += f'\n  {attribute}: ' # attribute label
        val = obj.__getattribute__(attribute) # value of attribute (will not necesarrily be printed)

        # will output a list of objects as a list of strings represented by the def_attr values of 
        if type(val) == list: 
            d_val = []          
            for i, item in enumerate(val):
                try:
                    d_val.append(item.__getattribute__(def_attr))
                except AttributeError:
                    d_val.append(item)
        elif type(val) != list and type(val) != tuple and type(val) != str and type(val) != int:
            d_val = val.repr_indent(indent + 2)
        else:
            d_val = val

        out += str(d_val)
    
    return out

def find_room(world, area_name, room_name = ''):   
    ret = []
    
    # find area that matches given area name
    i, a = find_by_attr(world.areas, "name", area_name, case_sensitive=False)
    if i == -1:
        ret.append(None)
        return ret, f"Could not find area: '{area_name}' in world"
    
    ret.append(a)
        
    if room_name != '':
        i, r = find_by_attr(ret[0].rooms, "name", room_name, case_sensitive=False)
        if i == -1: 
            return ret, f"Could not find room: '{room_name}' in area: '{area_name}' in world"
        ret.append(r)

    
    return ret, f"Found room: '{area_name}', '{room_name}'"

def find_by_attr(find_in, attr, attr_val, case_sensitive = True):
    if isinstance(find_in, list):
        tup_list = enumerate(find_in)
    elif isinstance(find_in, dict):
        tup_list = find_in.items()
    else: 
        return -1, Class()
    
    for index, item in tup_list:
        if case_sensitive or not isinstance(item.__getattribute__(attr), str):
            a = item.__getattribute__(attr)
        else:
            a = item.__getattribute__(attr).lower()
        val = attr_val if case_sensitive or type(attr_val) != str else attr_val.lower()
        if a == val:
            return index, item
    
    return -1, Class()