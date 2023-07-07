from app.Models import Audio
import shutil
import datetime
import os

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

def outdata(request):

    data = [
        i._toDict_ManageViews() for i in Audio.query.filter(Audio.is_delete == False).all()
    ]
    out = []

    for i in range(len(data)):
        out.append({
            "source_name": data[i]['source_name'],
            "storagefile_name": data[i]['storagefile_name'],
            "sort":i,
        })

    filename = datetime.datetime.strftime(datetime.datetime.now(), "audio_%Y%m%d_%H%M%S")
    os.makedirs(os.path.join(os.path.abspath('./save/' + filename + '/' )))

    for i in out:
        f, ext = QueryFileName(i['storagefile_name'])
        print(f)
        
        source_file = os.path.join(os.path.abspath('./app/static/audio/' ), i['storagefile_name'])
        target_file = os.path.join(os.path.abspath('./save/' + filename + '/' ), 'Audio_' + str(i['sort']) + ext)

        shutil.copy2(source_file, target_file)

    return 200, "", {}