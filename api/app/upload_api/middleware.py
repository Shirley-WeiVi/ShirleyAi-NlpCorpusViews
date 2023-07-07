#coding=utf-8
from functools import wraps
from flask import request
from app.Common import ReturnRequest

def UploadFile(func=None):
    """
    通用GET, POST请求, 不需要验证TOKEN, 只能使用application/json
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return ReturnRequest(func(request, *args, **kwargs))
    return wrapper