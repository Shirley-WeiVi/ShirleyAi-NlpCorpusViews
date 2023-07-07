# coding: utf-8
from app.Extensions import db
from datetime import datetime, timedelta
from config.runConfig import ProductionConfig
from config.storageConfig import StorageConfig


class BaseModel(object):
    
    """数据库表基类
        id， create_time， update_time

        可用变量:
            STATIC_LOADPATH：全局加载路径

        可用方法:
            delete, add, flush, commit, rollback

        事务:
            try:
                db.session.commit()
                return 200, msg, {"id":self.id}

            except Exception as e:
                print("事务异常>",e)
                db.session.rollback()
                return 400, "内部出错", {}

        base基础类
            BaseModel
            dict(
                **self._base()
            )
    """

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)                          # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)   # 记录的更新时间
    is_delete = db.Column(db.Boolean, default=False)    # 是否已经删除

    def _static_loadpath(self):
        """静态文件加载路径"""
        return ProductionConfig.STATIC_LOADPATH

    def _static_fileupload_path(self, uploadkey):
        """获取文件上传key的对应路径"""
        return StorageConfig.UPLOADFILE_CONFIG[uploadkey]

    def _id(self):
        return {"id":self.id}

    def _ct(self):
        return {"create_time":datetime.strftime(self.create_time, "%Y-%m-%d %H:%M:%S")}

    def _ut(self):
        return {"update_time":datetime.strftime(self.update_time, "%Y-%m-%d %H:%M:%S")}
    
    def _strftime(self, data):
        if not data:
            return None
        return datetime.strftime(data, "%Y-%m-%d %H:%M:%S")


class CorpusIndex(BaseModel, db.Model):
    
    __tablename__ = 'corpus_index'

    title = db.Column(db.String(250))                               # 可以是日期也可以是小分类

    def _toDict_ManageViews(self):
        return dict(
            title = self.title,
            id = self.id,
            session_count = CorpusSessionIndex.query.filter(CorpusSessionIndex.index_id == self.id, CorpusSessionIndex.is_delete == False).count()
        )

class CorpusSessionIndex(BaseModel, db.Model):
    
    __tablename__ = 'corpus_session_index'

    index_id = db.Column(db.Integer)                                # 索引ID

    def _toDict_ManageViews(self):

        obj = CorpusData.query.filter(CorpusData.is_delete == False, CorpusData.session_id == self.id).first()

        return dict(
            id = self.id,
            session_abstract = obj.data if obj else "None Data"
        )

class CorpusData(BaseModel, db.Model):
    
    __tablename__ = 'corpus_data'

    session_id = db.Column(db.Integer)                              # 会话ID
    data = db.Column(db.Text)                                       # 内容
    source_msg_data = db.Column(db.Text)                            # 内容
    questions_and_answers_type = db.Column(db.Integer)              # 1 是问 2是答

    def _toDict_ManageViews(self):
        return dict(
            data = self.data,
            id = self.id,
            questions_and_answers_type = self.questions_and_answers_type,
            source_msg_data = self.source_msg_data
        )

class Audio(BaseModel, db.Model):
    
    __tablename__ = 'audio_data'

    source_name = db.Column(db.String(250))                         # 源文件名
    second = db.Column(db.Integer)                                  # 时长 秒
    storagefile_name = db.Column(db.String(250))                    # 程序重命名后的文件名

    def _toDict_ManageViews(self):
        return dict(
            source_name = self.source_name,
            id = self.id,
            storagefile_name = self.storagefile_name,
            path = self._static_loadpath() + self._static_fileupload_path('audio') + self.storagefile_name
        )