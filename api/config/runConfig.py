class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ""
    SECRET_KEY = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'
    static_folder = 'static'
    RUNSERVER_PORT = 9001
    RUNSERVER_IP = '127.0.0.1'
    DEBUG = True
    STATIC_LOADPATH = "http://" + str(RUNSERVER_IP) + ":" + str(RUNSERVER_PORT) + "/apiService/Static"