import os
async def async_filewrite( filename, path, content, ):
    """
    :param filename:
    :param path:
    :param content:
    :return:
    """
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path,"\\", filename), 'w') as f:
        f.write(content)
        f.close()
        return True
def file_write(filename,path, content):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path,"\\", filename), 'w') as f:
        f.write(content)
        f.close()
        return True

def getUserDir():
    return os.path.expanduser("~")
async def asyncGetUserDir():
    return os.path.expanduser("~")

User = getUserDir()
