from typing import Literal
import requests
import re
__copyright__ = """
    Copyright (c) 2021 Ssword
    Authors of this software is not responsible for any damage caused by , indirectly caused by
    , or illegal use of this software. This software is provided "as is" without any express or implied
    warranty. Use at your own risk.
    Illegal use of this software may result in loss of privacy and companies taking
    legal actions against you. 
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software,
    to deal in the Software without restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
    and to permit persons to whom the Software is furnished to do so, subject to the following
    conditions:
    1. The above copyright notice and this permission notice shall be included in all copies or substantial
    portions of the Software.
    2. The software must not be blamed for any uses of this software from the user's usage
    of this software.
    3. Direct access to this software is provided under the terms of the copyright, permission is granted to access the file's contents
    4. The authors and contributors and stakeholders of this software have no responsibility or liability for the use of this software in any way,
    including, but not limited to, any damages caused by, indirectly caused by,
    or illegal use of this software.
    5. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote 
    products derived from this software without specific prior written permission.
    
    Patch Version:
    - 1.0.1 - Added support for asynchronous and synchronous filereading operations
    - 1.0.2 - Added Copyright notice




"""
async def async_readfile( filename_or_link:str, fileType:Literal["local file", "link"] ):

    """
    Read a file from the local filesystem or a link.
    """
    filename_not_filepath = re.split(r'[/\\]', filename_or_link)[-1]
    if filename_not_filepath.startswith('os') or filename_not_filepath.startswith('win'): 
        # i placed this here since i dont wanna get bonked by windows
        print("You do not have permission to read this file as it is an os file")
        raise PermissionError("You do not have permission to read this file")
    try:
        if fileType == "local file":
            with open(filename_or_link,"r") as f:
                return f.read()
        elif fileType == "link":
            r = requests.get(filename_or_link)
            return r.text
        else:
            raise ValueError("fileType must be 'local file' or 'link'")
    
        return None
    except PermissionError:
        print("You do not have permission to read this file")
        return None
    except FileExistsError as d:
        print("File does not exist")
        return None
    
    except FileNotFoundError as f:
        print("File cannot be found")
    except Exception as e:
        print(e)


def readfile( filename_or_link:str, fileType:Literal["local file", "link"]):
    """
    Read a file from the local filesystem or a link.
    """
    if fileType == "local file":
        with open(filename_or_link,"r") as f:
            return f.read()
    elif fileType == "link":
        r = requests.get(filename_or_link)
        return r.text
    else:
        raise ValueError("fileType must be 'local file' or 'link' therefore the operation is not valid.")

def help():
    print("""
    Functions such as readfile, async_readfile are Designed to be used for easy filereading.
          readfile:
                - Synchronous
          async_readfile:
                - Asynchronous
          usage: 
          file_content = readfile(filename, "local file")
          or 
          file_content = await async_readfile(filename, "local file")

""")
def Copyright():
    print(__copyright__)
