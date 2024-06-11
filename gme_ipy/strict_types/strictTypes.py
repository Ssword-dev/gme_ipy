from collections.abc import Iterator
import math
class StrictType:
    def __init__(self, errno, errmsg, errtype):
        self.errno = errno
        self.errmsg = errmsg
        self.errtype = errtype
        self.error = None
        self.error_encountered = {}
    def __del__(self):
        if self:
            del self
    def __str__(self):
        return self.errmsg
    def __type_check__(self, obj, type):
        if self:
            if not isinstance(obj, type):
                self.error_encountered[obj.name] = True
                self.error = self.errtype(self.errno, self.errmsg, type)
                return False
            return True
    def __del_if_not__(self, obj, type):
        if not self.__type_check__(obj, type):
            del obj
            return False
        else:
            return True # so it can be used as a truthy value on if else
    def __factory__(self):
        return self.__type_check__ # so it can be used as a variable
    
class PartialType(type):
    def __new__(cls, name, bases, dct):
        if 'PartialTyping' in dct:
            dct['__annotation__'] = dct['PartialTyping']
            def destruct_self(self):
                del self
            dct['__destruct__'] = destruct_self
        return super().__new__(cls, name, bases, dct)

class _FinalTyping(type):
    def __new__(cls, name, bases, dct):
        def __init_subclass__(self):
            raise TypeError("Final typings cannot be subclassed") # LMAO bro really tried to subclass
        def __del__(self):
            del self
        
        dct['__init_subclass__'] = __init_subclass__ # Replace __init_subclass__ with the new one
        dct['__del__'] = __del__ # Also add a method to delete self
        return super().__new__(cls, name, bases, dct)

class Extint(int):
    def __init__(self, ref):
        self.ref = ref
    def __sqrt__(self):
        return self.ref ** 2
    def __add__(self, other):
        return self.ref + other
    def __sub__(self, other):
        return self.ref - other
    def __mul__(self, other):
        return self.ref * other
    def __truediv__(self, other):
        return self.ref / other
    def __floordiv__(self, other):
        return self.ref // other
    def __rad__(self):
        return self.ref/ 2# the diameter is self.ref
    def __diameter__(self):
        return (self.ref) # self.ref is the diameter
    def __area__(self):
        return math.pi * ((self.ref / 2) ** 2)
    def __isequal__(self, other):
        return self.ref == other
    def __isless__(self, other):
        return self.ref < other
    def __isgreater__(self, other):
        return self.ref > other
    def __islessorequal__(self, other):
        return self.ref <= other
    def __isgreaterorequal__(self, other):
        return self.ref >= other
    def __isnotequal__(self, other):
        return self.ref != other
    def __isnotless__(self, other):
        return not self.ref < other
    def __isnotgreater__(self, other):
        return not self.ref > other
    def __isnotlessorequal__(self, other):
        return not self.ref <= other
    def __isnotgreaterorequal__(self, other):
        return not self.ref >= other

class Extstr(str):
    """
    An Extension of Python's built-in string data type
    """
    def __init__(self, ref:str):
        self.ref = ref
    def char(self):
        return [iters for iters in self.ref]
    def lenisequal(self, other):
        return len(self.ref) == other
    def lenisless(self, other):
        return len(self.ref) < other
    def lenisgreater(self, other):
        return len(self.ref) > other
    def _count(self):
        return len(self.ref)
    def inverse(self):
        return self.ref[::-1]
    def toUint(self):
        _ = []
        for char in self.ref:
            _.append(ord(char))
        return _
    def toInt(self):
        _ = []
        for char in self.ref:
            if char.isdigit():
                _.append(int(char))
        return _
class Extfloat(float):
    def __init__(self, ref):
        self.ref = ref
    def round(self):
        return round(self.ref)
    def floor(self):
        return math.floor(self.ref)
    def ceil(self):
        return math.ceil(self.ref)
    def mod(self, places):
        """
        >>> import math
        >>> pi_rnd = Extfloat(math.pi)
        >>> pi_rnd.mod(2)
        >>> print(pi_rnd)
stdout  <<< 3.14 
        """
        return float(f"{self.ref:{places}f}")
    def toexttint(self):
        return Extint(int(self.ref))

class Extlist(list):
    def __init__(self, ref:list):
        self.ref = ref
        self.strict_list_type = None
    def __reverse__(self):
        return self.ref[::-1]
    def sort(self,key):
        return self.ref.sort(key)
    def reverse_sort(self,key):
        return self.ref.sort(key, reverse=True)
    def __len__(self):
        return len(self.ref)
    def __getitem__(self, index):
        return self.ref[index]
    def __setitem__(self, index, value):
        self.ref[index] = value
    def __delitem__(self, index):
        del self.ref[index]
    def append_item(self, item):
        self.ref.append(item)
    def delete_self(self):
        del self
    def set_strict_list_type(self, type):
        """Set the strict list type, which can be used to control the list's item type and do a purge"""
        self.strict_list_type = type
    def enforce_strict_list_type(self):
        """
        Category: Filter or Strict list type
        """
        for item in self.ref:
            if not isinstance(item, self.strict_list_type):
                self.ref.remove(item)
            else:
                continue
class Exttuple(tuple):
    def __init__(self, ref:tuple):
        self.ref = ref
    def __len__(self):
        return len(self.ref)
    def __iter__(self) -> Iterator:
        return super().__iter__()
    def __getitem__(self, index):
        return self.ref[index]
    def __setitem__(self, index, value):
        new_ref = ()
        ptr = 0
        for item in self.ref:
            if ptr == index:
                new_ref += (value,)
            else:
                new_ref += (item,)
            ptr += 1
    def __delitem__(self, index):
        new_ref = ()
        ptr = 0
        for item in self.ref:
            if ptr == index:
                continue
            else:
                new_ref += (item,)
            ptr += 1
        self.ref = new_ref
    def append_items(self,*, items):
        for itm in items:
            self.ref += (itm,)
    def delete_self(self):
        del self
    def set_strict_tuple_type(self, type):
        """Set the strict tuple type, which can be used to control the tuple's item type and do a purge"""
        self.strict_tuple_type = type
    def enforce_strict_tuple_type(self):
        for item in self.ref:
            if not isinstance(item, self.strict_tuple_type):
                del self
                break

            else:
                continue
