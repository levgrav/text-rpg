import os


def explore(obj, def_attr: str = 'name'):
    
    os.system('cls')
    
    print(f"{obj.__getattribute__(def_attr)}")
    for attribute in obj.__dict__.keys():
        print(f'  {attribute}')

    thing = input("\nWhich attribute would you like to look at?\n")
    try:
        attribute = obj.__getattribute__(thing)


    except AttributeError:
        attribute = 'AttributeError'
    
    print(f"\nType: {type(attribute)}\n")

    if type(attribute) == str:
        print(attribute)
    elif type(attribute) == list:
        if attribute.__len__() == 0:
            print('Empty list')            
        else:
            try:
                for value in attribute:
                    print(value.__getattribute__(def_attr))
                
                choice = input('\nChoose one of the above: ')
                for value in attribute:
                    if value.__getattribute__(def_attr) == choice:
                        explore(value, def_attr)
                        break
                else:
                    print("\nNot found")
            except AttributeError:
                for value in attribute:
                    print(value)
    else:
        print('Unknown Type')

    input('\nPress <enter> to continue')


def get_attr(obj, attr_name:str, class_types: list, **kwargs):
    if attr_name not in obj.__dict__.keys():
        return 
    
    attr = obj.__getattribute__(attr_name)

    for class_type in class_types:
        if isinstance(attr, class_type):
            match class_type:
                case list, tuple:
                    return attr[:kwargs['length']], class_type
                case int, str:
                    return attr, class_type
                case dict:
                    return [attr[key] for key in kwargs['keys']], class_type

def set_attr(obj: object, attr_name, class_type, **kwargs):
    match class_type:
        case list, tuple:
            obj.__setattr__(attr_name, class_type(kwargs['values']))
        case int, str:
            obj.__setattr__(attr_name, class_type(kwargs['value']))
        case dict:
            obj.__setattr__(attr_name, {key : value for key, value in zip(kwargs['keys'], kwargs['values'])})

def disp_obj(obj: object, def_attr):
    msg = ''
    if need_attrs(obj, def_attr):
        return f"Bad def_attr: '{def_attr}'"
   
    msg += obj.__getattribute__(def_attr)

    for attribute in obj.__dict__.keys():
        msg += f'\n  {attribute}: '
        val = obj.__getattribute__(attribute)

        if type(val) == list: 
            d_val = []          
            for i, item in enumerate(val):
                try:
                    d_val.append(item.__getattribute__(def_attr))
                except AttributeError:
                    d_val.append(item)
        else:
            d_val = val
        msg += str(d_val)
    
    return msg

def need_attrs(obj, *attrs):
    for attr in attrs:
        if attr not in obj.__dict__.keys():
            return attr
    
    return None

def find_room(world, area_name, room_name = None):    
    # needs attribute 'areas'
    r = [None, None]
    if need_attrs(world, "areas") != None:
        msg = f"World needs attribute 'areas' to use the function 'find_area_room'"
        return r, msg
    
    # find area that matches given area name
    for area in world.areas:
        if area.name == area_name:
            r[0] = area
            break
    else: 
        msg = f"Could not find area: '{area_name}' in world"
        return r, msg

    if room_name != None:
        for room in area.rooms: # type: ignore
            if room.name == room_name:
                r[1] = room
                break
        else: 
            msg = f"Could not find room: '{room_name}' in area: '{area_name}'"
            return r, msg
    
    msg = f"Found room: '{area_name}', '{room_name}'"
    return r, msg