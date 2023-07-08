from app.Models import CorpusIndex, CorpusSessionIndex, CorpusData
import json
import datetime
import os
import shutil

def split_list_into_pairs(lst):
    return [lst[i:i+2] for i in range(0, len(lst), 2)]

def outdataset(request):

    out = []
    filename = datetime.datetime.strftime(datetime.datetime.now(), "corpus_%Y%m%d_%H%M%S")
    os.makedirs(os.path.join(os.path.abspath('./save/' + filename + '/' )))
    os.makedirs(os.path.join(os.path.abspath('./save/' + filename + '/msg_emoji' )))
    os.makedirs(os.path.join(os.path.abspath('./save/' + filename + '/msg_image' )))

    # 取出正常的索引
    index_data = CorpusIndex.query.filter(CorpusIndex.is_delete == False).all()

    # 取出每个索引集下的会话集
    for i in index_data:
        print("index>> ", i.id, i.title)
        session_set = CorpusSessionIndex.query.filter(CorpusSessionIndex.index_id == i.id, CorpusSessionIndex.is_delete == False).order_by(CorpusSessionIndex.create_time.desc()).all()

        # 取出每个会话集下的数据
        for s in session_set:

            limit = []
            history = []
            validation_dataset = []
            print("session>> ", s.id)

            # 获取会话集下的数据
            data = CorpusData.query.filter(CorpusData.session_id == s.id, CorpusData.is_delete == False).order_by(CorpusData.create_time).all()
            
            for d in data:
                if d.msg_type == 1:
                    limit.append({
                        "data": d.data
                    })

                if d.msg_type == 2:
                    limit.append({
                        "data": "EMOJI:" + d.emoji_file
                    })

                    source_file = os.path.join(os.path.abspath('./app/static/msg_emoji/' ), d.emoji_file)
                    target_file = os.path.join(os.path.abspath('./save/' + filename + '/msg_emoji/' ), d.emoji_file)

                    shutil.copy2(source_file, target_file)

                if d.msg_type == 3:
                    limit.append({
                        "data": "IMAGE:" + d.image_content
                    })

                    source_file = os.path.join(os.path.abspath('./app/static/msg_image/' ), d.image_file)
                    target_file = os.path.join(os.path.abspath('./save/' + filename + '/msg_image/' ), d.image_file)

                    shutil.copy2(source_file, target_file)

            data = split_list_into_pairs(limit)

            for i in range(len(data)):
                if i == 0:
                    validation_dataset.append([data[i][0]['data'], data[i][1]['data'], []])
                else:
                    validation_dataset.append([data[i][0]['data'], data[i][1]['data'], history[:]])

                history.append(data[i][0]['data'])
                history.append(data[i][1]['data'])
                
            for v in validation_dataset:
                out.append({
                        "prompt": v[0],
                        "response": v[1],
                        "history": v[2]
                    })

    

    with open('./save/' + filename + '/' + filename + '.json', 'w', encoding='utf-8') as json_file:

        for o in out:

            print(o)
            json_file.write(json.dumps(o, ensure_ascii=False) + '\n')


    return 200, 0, {}