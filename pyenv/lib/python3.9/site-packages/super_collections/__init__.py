"""
Super Collections

Their purpose is to turn complex input such as json or YAML files into
Python objects accessible with attributes, and self documented.

The general idea is that those structured files are combinations
of lists and dictionaries.

(C) Laurent Franceschetti 2024
"""
import datetime
import json
import inspect
from typing import Any


import hjson

# -------------------------------------
# Low-level fixtures
# -------------------------------------
from collections import UserDict

DICT_TYPES = dict, UserDict

class CustomEncoder(json.JSONEncoder):
    """
    Custom encoder for JSON serialization.
    Used for debugging purposes.
    """
    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, UserDict):
            # for objects used by some packages
            return dict(obj)

        elif inspect.isfunction(obj):
            return f"Function: %s %s" % (inspect.signature(obj),
                                        obj.__doc__)
        try:
            return super().default(obj)
        except TypeError:
            print(f"CANNOT INTERPRET {obj.__class__}")
            return str(obj)


# -------------------------------------
# Collections
# -------------------------------------
class SuperDict(dict):
    """
    A dictionary with key accessibles as properties
    (with the dot notation)

    a['foo'] <=> a.foo

    As a rule, the Superdict will expose as properties
    all keys that:

    1. Are valid identifiers
    2. Are not a standard property or method of the dict, 
        class notably:
        attributes, clear, copy, fromkeys, get, items,
        keys, pop, popitem, setdefault, update, values

    Lists in a SuperDict are converted into SuperLists, whose elements
    are in turn converted, etc...
    """

    def __init__(self, *args, **kwargs):
        # Call the superclass's __init__ method
        super().__init__(*args, **kwargs)
        self.__post_init__()

    def __post_init__(self):
        "Recursively transform sub-dictionary"
        for key, value in self.items():
            if isinstance(value, SUPER_TYPES):
                pass
            elif isinstance(value, DICT_TYPES):
                self[key] = SuperDict(value)
            elif isinstance(value, list):
                self[key] = SuperList(value)

    def __getattr__(self, name:str):
        "Allow dot notation on reading"
        ERR_MSG = "Cannot find attribute '%s'" % name
        # if name.startswith('_'):
        #     raise AttributeError(ERR_MSG)
        try:
            return self[name]
        except KeyError:
            raise AttributeError(ERR_MSG)



    def properties(self):
        """
        Generate the valid properties
        (the dictionary keys that qualify as Python identifiers
        and are not callables)
        """
        return (item for item in self.keys() 
                if isinstance(item, str)
                    and item.isidentifier()
                    and not callable(getattr(self, item)))
    

    
    def __dir__(self):
        "List all attributes (for autocompletion, etc.)"
        return super().__dir__() + list(self.properties())
    
    # -------------------------------------
    # Output
    # -------------------------------------


    def __setattr__(self, name, value):
        "Allow dot notation on writing"
        # ERR_MSG = "Cannot assign an attribute starting with _ ('%s')" % name
        # if name.startswith('_'):
        #     raise AttributeError(ERR_MSG)     
        self[name] = value


    def update(self, other:dict):
        """
        Update the SuperDict with another.

        If necessary the other dictionary is converted into a SuperDict
        """
        if not isinstance(other, SuperDict):
            other = SuperDict(other)
        return super().update(other)
    
    
    # -------------------------------------
    # Output
    # -------------------------------------
    
    def to_json(self):
        """
        Convert to json.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        return json.dumps(self, cls=CustomEncoder)
    
    def to_hjson(self):
        """
        Convert to hjson.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        python_dict = json.loads(self.to_json())
        return hjson.dumps(python_dict)


    def __str__(self):
        "Print a superdict"
        return self.to_hjson()
    
    def __rich__(self):
        "Print a superdict (for rich)"
        r = [f"[bold red]{self.__class__.__name__}:[/]"]
        r.append(self.to_hjson())
        return("\n".join(r))       




class SuperList(list):
    """
    A list that supports the SuperDict,
    to allow recursion within complex structures
    """

    def __init__(self, *args, **kwargs):
        # Call the superclass's __init__ method
        super().__init__(*args, **kwargs)
        self.__post_init__()

    def __post_init__(self):
        "Recursively transform sub-list"
        for index, value in enumerate(self):
            if isinstance(value, SUPER_TYPES):
                pass
            elif isinstance(value, DICT_TYPES):
                self[index] = SuperDict(value)
            elif isinstance(value, list):
                self[index] = SuperList(value)



    # -------------------------------------
    # Modify
    # -------------------------------------

    def extend(self, l):
        "Extend the list with another one (transforms it first in SuperList)"
        l = SuperList(l)
        super().extend(l)

    def __add__(self, l):
        "Addition with another list"
        l = SuperList(l)
        return SuperList(super().__add__(l))
    # -------------------------------------
    # Output
    # -------------------------------------
    
    def to_json(self):
        """
        Convert to json.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        return json.dumps(self, cls=CustomEncoder)
    
    def to_hjson(self):
        """
        Convert to hjson.

        It does not have any claim of fitness for any
        particular purpose, except showing what's in structure,
        for string output.
        """
        python_dict = json.loads(self.to_json())
        return hjson.dumps(python_dict)


    def __str__(self):
        "Print a superdict"
        return self.to_hjson()
    
    def __rich__(self):
        "Print a superdict (for rich)"
        r = [f"[bold red]{self.__class__.__name__}:[/]"]
        r.append(self.to_hjson())
        return("\n".join(r))     

SUPER_TYPES = SuperDict, SuperList