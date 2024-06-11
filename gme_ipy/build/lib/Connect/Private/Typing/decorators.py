import typings
from typing import Callable
import random
def ExpectedToBe(func,expected_typing:typings.TypeDeclarations):
    """
    Decorator to check if the return value of a function is of a certain type.
    """
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        if isinstance(result, expected_typing):
            return result
        else:
            raise TypeError(f"Expected {expected_typing.__name__} but got {type(result).__name__}")
        
    return wrapper
def ExpectedToNotBe(self, expected_typing:typings.TypeDeclarations) -> Callable:
    """
    Decorator to check if the return value of a function is not of a certain type.
    """
    def wrapper(*args,**kwargs):
        result = self(*args,**kwargs)
        if not isinstance(result, expected_typing):
            return result
        else:
            raise TypeError(f"Expected not {expected_typing.__name__} but got {type(result).__name__}")
        
    return wrapper
def TurnTo(self, type_):
    """
    Decorator to turn the return value of a function to a certain type.
    """
    def wrapper(*args,**kwargs):
        result = self(*args,**kwargs)
        if isinstance(result, type):
            return result
        else:
            return type_(result)
    
    return wrapper
def Randomize(self):
    """Generates a random string using a decorator host function"""
    ord_list = []
    result = str(self())
    for c in result:
        ord_list.append(ord(c) + random.randint(0,64))
    return ''.join([chr(i) for i in ord_list])
def destruct(cls, after: int):
    """
    Decorator to destruct the class after the `{after:int}` limit was reached.
    """
    class Meta(type):
        def __call__(self, *args, **kwargs):
            if not hasattr(self, 'instantiated'):
                self.instantiated = 0

            if self.instantiated >= after:
                raise Exception(f"The class {cls.__name__} was destructed after {self.instantiated} instantiations")
            
            self.instantiated += 1
            return super().__call__(*args, **kwargs)
    
    # Attach the metaclass to the class
    cls.__class__ = Meta(cls.__name__, cls.__bases__, dict(cls.__dict__))
    return cls
class __MakeMetaclass():
    """
    A function that creates a metaclass, self should be the variable name of the instance
    """
    def __init__(self,__new__, class_name):
        class Meta(type):
            def __new__(cls, name, bases, dct):
                return __new__(cls,bases=bases, name=name, dct=dct)
        Meta.__name__ = class_name
        self.meta = Meta
    def __call__(self):
        return self.meta
def __access_global_dict():
    return globals()

def __access_local_dict():
    return locals()
def MakeMetaClass(__new__,name):
    """
    Params:
        - __new__ : metaclass's new method
        - name : metaclass's name
    ~~~~~
    Returns:
        - Metaclass
    ~~~~~
    Usage::\n
    Unity = MakeMetaClass(__new_method_func__, "Unity")
    """
    try:
        newMetaClass = __MakeMetaclass(__new__,name)
        GlobalVars = __access_global_dict()
        GlobalVars[name]= newMetaClass()
        return newMetaClass()
    except ValueError:
        print("Could not create new metaclass")
    except Exception as f:
        print(f"Error occured while creating new MetaClass, Error reference:\n {f}")

def test(cls,name,bases,dct):
    print(name)
    print(bases)
    print(cls.__name__)
    return type.__new__(cls,name,bases,dct)
newMeta = MakeMetaClass(test, "newMeta")
class Test(metaclass=newMeta):
    def __call__(self, *args, **kwds) -> None:
        pass