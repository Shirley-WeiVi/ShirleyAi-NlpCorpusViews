from app.Models import Audio
from app.Extensions import db

def create(request):

    add = Audio()
    add.source_name = request.get('source_name',None)
    add.storagefile_name = request.get('storagefile_name',None)

    try:
        db.session.add(add)
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}

def query(request):
    data = [
        i._toDict_ManageViews() for i in Audio.query.filter(Audio.is_delete == False).all()
    ]
    out = []
    for i in range(len(data)):
        out.append({
            "data":data[i],
            "sort":i
        })
    return 200, "", out

def delete(request):

    fileid = request.get('fileid',None)
    
    if not fileid:
        return 400, "fileID不能为空", {}
    
    obj = Audio.query.get(fileid)

    if not obj:
        return 400, "对象不存在", {}

    obj.is_delete = True

    try:
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}