from typing import TypeVar, Union,Type, Literal, Callable,Final,final
import warnings

"""
Since Typings do nothing at runtime, this will also do nothing on runtime
"""
_T = TypeVar("_T")
char = str # A single string character

Iterables = Union[set, tuple,list,map,dict,str]# Yes, strings are also iterable,its a set of characters
__Subclass_signature = Type[_T]
SubClassing = __Subclass_signature
SubClass = Type

PrimitiveTypes = Union[char,int,float,type,bool,Iterables]
BuiltInTypings = Union[PrimitiveTypes]
ImmutableIterables = Union[tuple]
TypeDeclarations = Union[Type,type]
AnyType = Union[object, type]
Numbers = Union[int,float,SubClass[float],SubClass[int]]
"""
>>>  {
    "type" : Union[int,float,SubClass[float],SubClass[int]]
}
"""
key = Union[object, str, int]
"""
Represents a dict key, such as string keys, int keys
"""
EscapeCode = Union[Literal["\n","\t","\\",
    "\'","\"","\r","\b","\f","\v","\0","\u0000","\U00000000"
]]
class Class(dict):"""Generic Class Type"""
class __init__(Callable, Class):"""Generic Class Constructor"""
class __method__(Callable, Class):"""Generic Class Method"""
class __del__(Callable, Class):"""Generic Class Delete Method"""
class Error(Exception):"""Generic Error type"""
class RegexString(str):"""Generic Regex String"""
class Wrapper(Callable, Class):"""Generic Wrapper Function"""
class GenericObject(Callable,Class,object):"""Generic Object"""
