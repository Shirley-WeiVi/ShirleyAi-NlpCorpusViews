from app.Models import CorpusData
from app.Extensions import db


def data_text_create(request):

    session_id = request.get('session_id',None)
    questions_and_answers_type = request.get('questions_and_answers_type',None)

    source_msg_data = request.get('source_msg_data',None)
    data = request.get('data',None)

    if not data or not source_msg_data:
        return 400, "内容不能为空", {}

    if not session_id:
        return 400, "索引ID不能为空", {}
    
    if int(questions_and_answers_type) not in [1,2]:
        return 400, "类型错误", {}

    add = CorpusData()
    add.session_id = session_id
    add.data = data
    add.source_msg_data = source_msg_data
    add.questions_and_answers_type = questions_and_answers_type
    add.msg_type = 1

    try:
        db.session.add(add)
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}


def data_emoji_create(request):
    
    session_id = request.get('session_id',None)
    questions_and_answers_type = request.get('questions_and_answers_type',None)

    storagefile_name = request.get('storagefile_name',None)

    if  not storagefile_name:
        return 400, "内容不能为空", {}

    if not session_id:
        return 400, "索引ID不能为空", {}
    
    if int(questions_and_answers_type) not in [1,2]:
        return 400, "类型错误", {}

    add = CorpusData()
    add.session_id = session_id
    add.emoji_file = storagefile_name
    add.questions_and_answers_type = questions_and_answers_type
    add.msg_type = 2

    try:
        db.session.add(add)
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}


def data_image_create(request):
    
    session_id = request.get('session_id',None)
    questions_and_answers_type = request.get('questions_and_answers_type',None)

    image_content = request.get('image_content',None)
    storagefile_name = request.get('storagefile_name',None)

    if  not storagefile_name or not image_content:
        return 400, "内容不能为空", {}

    if not session_id:
        return 400, "索引ID不能为空", {}
    
    if int(questions_and_answers_type) not in [1,2]:
        return 400, "类型错误", {}

    add = CorpusData()
    add.session_id = session_id
    add.questions_and_answers_type = questions_and_answers_type
    add.image_file = storagefile_name
    add.image_content = image_content
    add.msg_type = 3

    try:
        db.session.add(add)
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}


def data_query(request):

    session_id = request.get('session_id',None)
    
    if not session_id:
        return 400, "会话ID不能为空", {}

    return 200, "", {
        "data":[
            i._toDict_ManageViews() for i in CorpusData.query.filter(CorpusData.session_id == session_id, CorpusData.is_delete == False).order_by(CorpusData.create_time).all()
        ],
        "datacount": CorpusData.query.filter(CorpusData.session_id == session_id, CorpusData.is_delete == False).order_by(CorpusData.create_time).count()
    }


def data_delete(request):
    
    dataid = request.get('dataid',None)

    if not dataid:
        return 400, "数据ID不能为空", {}

    obj = CorpusData.query.get(dataid)

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
    

def data_withdraw(request):

    session_id = request.get('session_id',None)

    if not session_id:
        return 400, "会话ID不能为空", {}

    obj = CorpusData.query.filter(CorpusData.session_id == session_id, CorpusData.is_delete == False).order_by(CorpusData.create_time.desc()).first()

    if not obj:
        return 400, "无消息可撤回", {}

    obj.is_delete = True

    try:
        db.session.commit()
        return 200, "成功", {}

    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return 400, "内部出错", {}