from app.Models import CorpusIndex, CorpusSessionIndex, CorpusData
import json
import datetime

def outdataset(request):

    validation_dataset = []

    # 取出正常的索引
    index_data = CorpusIndex.query.filter(CorpusIndex.is_delete == False).all()

    # 取出每个索引集下的会话集
    for i in index_data:
        session_set = CorpusSessionIndex.query.filter(CorpusSessionIndex.index_id == i.id, CorpusData.is_delete == False).order_by(CorpusData.create_time.desc()).all()

        for i in session_set:

            # 获取会话集下的数据
            data = CorpusData.query.filter(CorpusData.session_id == i.id, CorpusData.is_delete == False).all()
            limit = []

            for i in data:
                limit.append({
                    "data": i.data
                })

            start, end = 0, 0
            msg, history = [], []

            for i in range(len(limit)):

                if int(len(limit))/2 == i:
                    break

                if end == 0:
                    start = i
                    end = i + 2

                else:
                    start = start + 2
                    end = start + 2

                msgdata = {
                        "prompt": limit[start:end][0]['data'],
                        "response": limit[start:end][1]['data'],
                        "history": history[0:i] if int(len(history)) > 0 else []
                    }

                msg.append(msgdata)

                history.append([limit[start:end][0]['data'], limit[start:end][1]['data']])

                print(i, start, end, msgdata)

            validation_dataset = validation_dataset + msg
            

    print(validation_dataset)
    filename = datetime.datetime.strftime(datetime.datetime.now(), "corpus_%Y%m%d_%H%M%S") + '.json'

    with open('./save/' + filename, 'w', encoding='utf-8') as json_file:

        for i in validation_dataset:
            
            print(json.dumps(i))
            json_file.write(json.dumps(i, ensure_ascii=False) + '\n')
            # json.dump(json.dumps(i) + '\n', json_file)


    return 200, 0, {}