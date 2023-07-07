import hashlib
import os
import random
from datetime import datetime
from io import *
from config.storageConfig import StorageConfig
from config.runConfig import ProductionConfig

"""
    关于 UPLOADFILE_CONFIG的用法
    key: 上传文件的时候必须附带的参数uploadKey : 此处设置的key
    value: 上传的文件根据key获取储存的路径 比方说 'head':'image', 表示携带head上传的文件需要储存到image路径下
"""


def CreateNewFilename(ext):
    """生成新的随机文件名
    Args:
        ext: str, 文件后缀名

    Returns:
        生成的随机字符串 + 后缀名

    """
    return datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + '{:03d}'.format(random.randint(0, 999)) + ext


def QueryFileName(filestr):
    """分割文件名

    Args:
        filestr: str, 完整文件名

    Returns:
        文件名, 后缀名
        example:
            xxx, .jpg

    """
    pach, filename = os.path.split(filestr)
    return os.path.splitext(filename)


def FileExtLegitimate(ext, upload_key):
    """判断文件类型是否允许上传

    """
    if ext:
        if upload_key not in StorageConfig.UPLOADFILE_ALLOEWTYPE:
            return False
        
        if ext not in StorageConfig.UPLOADFILE_ALLOEWTYPE[upload_key]:
            return 
        
        return True

    else:
        return False


def upload_file(request):

    try:
        file = request.files['file']
    except:
        return 400, '错误: 没有文件', ''

    upload_key = request.form.get('uploadKey', None)
    if not upload_key:
        return 400, '错误: Key值不能为空', {}

    if upload_key not in StorageConfig.UPLOADFILE_CONFIG:
        return 400, '错误: 不允许使用的Key值', {}

    filename, ext = QueryFileName(file.filename)
    
    print(ext, upload_key)
    if not FileExtLegitimate(ext, upload_key):
        return 400, '文件类型不允许', {}
    
    newfilename = CreateNewFilename(ext)

    # 保存文件到服务器
    file.save(os.path.join(os.path.abspath('app/static' + StorageConfig.UPLOADFILE_CONFIG[str(upload_key)] ), newfilename))

    # 加载地址
    try:
        LOADPATH = ProductionConfig.STATIC_LOADPATH

    except Exception as e:
        print(e)
        LOADPATH = ""

    return 200, 'ok', {
        'lodpath': LOADPATH + StorageConfig.UPLOADFILE_CONFIG[str(upload_key)] + newfilename,
        'ospath': StorageConfig.UPLOADFILE_CONFIG[str(upload_key)] + newfilename,
        'filename': newfilename,
        'sourcefilename': str(filename) + str(ext)
    }
