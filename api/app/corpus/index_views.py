from app.Models import CorpusIndex
from app.Extensions import db


def index_create(request):

    title = request.get('title',None)

    if not title:
        return 400, "索引名不能为空", {}

    add = CorpusIndex()
    add.title = title

    try:
        db.session.add(add)
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}


def index_query(request):
    
    return 200, "", [
        i._toDict_ManageViews() for i in CorpusIndex.query.filter(CorpusIndex.is_delete == False).all()
    ]


def index_update(request):

    index_id = request.get('index_id',None)
    title = request.get('title',None)

    obj = CorpusIndex.query.get(index_id)

    if not obj:
        return 400, "对象不存在", {}

    if title:
        obj.title = title

    try:
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}


def index_delete(request):
    
    index_id = request.get('index_id',None)

    if not index_id:
        return 400, "索引ID不能为空", {}

    obj = CorpusIndex.query.get(index_id)

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