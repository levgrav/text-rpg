from dataclasses import dataclass


@dataclass
class Class:
    def __init__(self, through_dict = True, **kwargs):

        for kw, arg in kwargs.items():
            if through_dict and isinstance(arg, dict):
                arg = Class(**arg)
            self.__setattr__(kw, arg)
    
    def __repr__(self):
        attrs = []
        for attr, val in self.__dict__.items():
            if val == None:
                val = "None"
            
            elif type(val) == int:
                val = str(val)
            
            elif type(val) != str:
                if 'name' in val.__dict__.keys():
                    val = val.name
            
            attrs.append(attr + ': ' + val) 

        s = ''
        for attr in attrs:
            s += attr + '\n'
        
        return s
    
    def repr_indent(self, indent) -> str:
        
        attrs = []
        for attr, val in self.__dict__.items():
            if val == None:
                val = "None"
            
            elif type(val) == int:
                val = str(val)
            
            elif type(val) != str:
                if 'name' in val.__dict__.keys():
                    val = val.name
            
            attrs.append(attr + ': ' + val) 

        s = ''
        for attr in attrs:
            s += '\n' + indent * "  " + attr
        
        return s