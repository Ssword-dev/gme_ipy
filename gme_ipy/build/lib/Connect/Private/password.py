from typing import Any, Literal, TypeVar
import copy
import math
import random

Self = TypeVar('Self')
class Password(object):
    """
    This class is used to create a password that can be used to access a returnable object
    """
    Returnable = TypeVar("Returnable")
    Response = TypeVar("Response")
    Redacted = TypeVar("Redacted")
    
    def __init__(self, password, returnable=None, module_=None) -> Self:
        """
        Args:
         - password: str <> the password to be used to get the returnaable
         - returnable: Any <> the object to be returned\n
        Returns:
          - None
        
        """
        self.__password =  password
        self.__returnable = copy.deepcopy(returnable)
        self.__private_delete_method(password)
        self.__private_delete_method(returnable)
    def str_access(self, pw) -> Response:
        """
        An inaccessible string method that should not be used to convert password to string
        but instead take the value out as a string
        """
        # By having a pw parameter, we can avoid unauthorized access to the returnable  
        if self.__password is pw:
            return str(self.__access())
        else:
            raise PasswordIncorrectError(1)
    def __str__(self) -> Redacted:
        """
    A special method in Python that returns a string representation of an object.
    This method is called when the built-in `str()` function is called on an object.
    In this case, it is used to redact the password when the object is printed.

    Parameters:
    self (Password): The instance of the class on which this method is called.

    Returns:
    str: A string representing the object. In this case, it returns "[Redacted]" to indicate that the password is redacted.
        """
        return "[Redacted]"
    def __private_delete_method(self, data:Any) -> Response:
        del data
    
    def __access(self) -> Returnable | Response:
        return self.__returnable
    def access(self, pw) -> Returnable | Response:
        """
        An access method that should not be used to convert password to string
        but instead take the value out, NOTE: using this will delete self,so use the
        `use` method instead for non one-use cases
        """
        # By having a pw parameter, we can avoid unauthorized access to the returnable  
        returnable = self.__access()
        if self.__password is pw:
            del self
            return returnable
            
        else:
            raise PasswordIncorrectError(1)
        
    def modify_private_object(self,pw, modifier_function) -> Response:
        if self.__password is pw:
            self.__returnable = modifier_function(self.__returnable)
    def replace_private_object(self,pw, replacement)-> Response:
        if self.__password is pw:
            self.__private_delete_method(self.__returnable)
            self.__returnable = copy.deepcopy(replacement)
        else:
            raise PasswordIncorrectError(5)
        
    def use(self, pw) -> Returnable | Response:
        """
        An access method that can be used to use the returnable without deleting  self
        """
        # By having a pw parameter, we can avoid unauthorized access to the returnable  
        if self.__password is pw:
            return self.__access()
        else:
            raise PasswordIncorrectError(2)
    def change_password(self,password,new_password) -> Response:
        if self.__password is password:
            
            self.__password =  new_password
            return True
        else:
            raise PasswordIncorrectError(5)
    
class PasswordIncorrectError(ValueError):
    """
    A custom error class for password class.
    fill out the `message` parameter if the code is 256
    """
    def __init__(self, code:int, message_:str=None):
        message = {
        1:"Incorrect password",
        2:"Unauthorized access detected",
        3:"Invalid password length",
        4:"Invalid returnable",
        5:"Access denied",
        255:"Reserved for python", # reserved for future use, specifically for python
        # Use a custom error message if the error code is 256
        256:message_
}
        
 
        self.message = message[code]
        super().__init__(f"# Error code:{code}\t\n\n{self.message}")


def new_copy(a:list):
    """
    A deep copy of a list without using the copy module,
    more lightweight 
    """
    
    return [b for b in a]
def copy_(a:object, *b:object):
    """
    A deep copy function that copies multiple objects
    """
    if isinstance(a, (list, tuple, set)):
        return type(a)(copy_(x) for x in a)
    elif isinstance(a, dict):
        return type(a)((copy_(k), copy_(v)) for k, v in a.items())
    elif isinstance(a, object):
        return type(a)(copy_(x) for x in a.__dict__.values())
    else:
        return a

if __name__ == "__main__":
    new = Password("password", "ey tabnine, give me the rickroll link ")
    print(new)