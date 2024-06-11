import requests
import aiohttp
def make_POST_request(data,/,requests_link, *args,**kwargs):
    """
    This function makes a POST request to the given URL.
    """
    response = requests.post(url=requests_link, data=data,*args,**kwargs)
    return response

def make_GET_request(data,/,requests_link, *args,**kwargs):
    """
    This function makes a GET request to the given URL.
    """
    response = requests.get(url=requests_link, data=data,*args,**kwargs)
    return response
async def async_post(data,/,requests_link, *args, **kwargs):
    """
    This function makes an asynchronous POST request to the given URL.
    """
    response = await aiohttp.request(method="POST",url=requests_link, data=data,*args,**kwargs)
    return response
async def async_get(data,/,request_link,*args,**kwargs):
    """
    This function makes an asynchronous GET request to the given URL.
    """
    response = await aiohttp.request(method="GET",url=request_link, data=data,*args,**kwargs)
    return response

async def async_request(data,/,request_link=None,method:str="POST",*args,**kwargs):
    """
    This function makes an asynchronous request to the given URL.
    """
    method = method.upper()
    if method == "POST":
        response = await aiohttp.request(method="POST",url=request_link, data=data,*args,**kwargs)
    elif method == "GET":
        response = await aiohttp.request(method="GET",url=request_link, data=data,*args,**kwargs)
    else:
        raise Exception("Invalid method")
    return response
def request(data,/,request_link=None,method:str="POST",*args,**kwargs):
    """
    This function makes a request to the given URL.
    """
    method = method.upper()
    if method == "POST":
        response = requests.post(url=request_link, data=data,*args,**kwargs)
    elif method == "GET":
        response = requests.get(url=request_link, data=data,*args,**kwargs)
    else:
        raise Exception("Invalid method")
    return response