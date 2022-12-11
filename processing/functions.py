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
