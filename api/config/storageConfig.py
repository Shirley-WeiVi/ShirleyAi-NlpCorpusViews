class StorageConfig:
    
    # 统一上传保存
    UPLOADFILE_CONFIG = {
        'audio': '/audio/',
        'emoji': '/msg_emoji/',
        'image': '/msg_image/',
    }

    # 不同的key值允许上传的文件类型
    UPLOADFILE_ALLOEWTYPE = {
        'audio':[
            '.wav','.mp3'
        ],
        'emoji':[
            '.png', '.jpg', '.gif'
        ],
        'image':[
            '.png', '.jpg', '.gif'
        ]
    }