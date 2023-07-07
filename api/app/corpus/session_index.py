from app.Models import CorpusSessionIndex
from app.Extensions import db


def session_create(request):

    index_id = request.get('index_id',None)

    if not index_id:
        return 400, "索引ID不能为空", {}

    add = CorpusSessionIndex()
    add.index_id = index_id
    try:
        db.session.add(add)
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}


def session_query(request):

    index_id = request.get('index_id',None)
    
    if not index_id:
        return 400, "索引ID不能为空", {}

    return 200, "", [
        i._toDict_ManageViews() for i in CorpusSessionIndex.query.filter(CorpusSessionIndex.index_id == index_id, CorpusSessionIndex.is_delete == False).all()
    ]


def session_delete(request):
    
    session_index_id = request.get('session_index_id',None)

    if not session_index_id:
        return 400, "索引ID不能为空", {}

    obj = CorpusSessionIndex.query.get(session_index_id)

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