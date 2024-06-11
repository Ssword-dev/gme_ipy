instances_ = {}

class StandAloneInstance(type):
    def __new__(cls, name, bases, dct, *args, **kwargs):
        if name not in instances_:
            instances_[name] = 0
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        """
        update the instance counter
        """
        if instances_[cls.__name__] < cls.instance_limit:
            instance = super().__call__(*args, **kwargs)
            instances_[cls.__name__] += 1
            return instance
        else:
            raise ValueError(f"{cls.__name__} instances are greater than {cls.instance_limit}")

class Example(metaclass=StandAloneInstance):
    instance_limit = 1
    
    def __init__(self):
        print("Example instance created")

try:
    sample1 = Example()
    sample2 = Example()
except ValueError as e:
    print(e)  
