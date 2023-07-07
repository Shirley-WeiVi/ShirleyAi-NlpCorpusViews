from app.upload_api import upload_api, views
from app.Common import ReturnRequest
from app.upload_api.middleware import UploadFile

# 上传文件
@upload_api.route('/file', methods=["POST"])
@UploadFile
def upload_file(request):
    """多用文件上传接口
    Args:
        file: 文件
        uploadKey: 上传的key值

    Returns:
        ospath, 系统内的储存路径 一般不用
        lodpath, 加载路径 带http路径 + /static + ospath, 一般用于上传完成后加载用
        filename, 文件名

    Raises:
        200 ok
        400 错误: 没有文件
            错误: Key值不能为空
            文件类型不允许
            错误: 不允许使用的Key值

    ReturnJson:
        {
            "code": 200,
            "data": {
                "filename": "20201012115423509.jpg",
                "lodpath": "http://127.0.0.1/static/head/20201012115423509.jpg",
                "ospath": "/head/20201012115423509.jpg"
            },
            "msg": "ok"
        }
    """
    return views.upload_file(request)