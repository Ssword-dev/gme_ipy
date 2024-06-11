"""
Now... why is this called "Private"..? this package allowes for private variables that cannot be
accessed by unauthorised users
"""

from . import (
    password,
    Typing,
    DotEnvProcessing
)

__all__ = [
    "password",
    "Typing",
    "DotEnvProcessing"
    ]