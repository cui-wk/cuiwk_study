#coding = utf-8
import json

def get_data_value(data,key):
    data = json.loads(data)
    dict_key = key.split('.')
    for i in dict_key:
        if isinstance(data,dict) or isinstance(data,list):
            data = data[i]
        else:
            data = json.loads(data)
            data = data[i]
    return data


if __name__ == "__main__":
    data = json.dumps({
    'aa':'111',
    'bb':"{\"id\":\"1ui2kdic9\",\"j1\":{\"dd\":\"dd4566\",\"uu\":\"uu\"},\"j2\":{\"33\":\"33\",\"66\":\"66\",\"j22\":{\"j0\":0},\"j23\":{\"00\":0}},\"name\":\"110\"}"
    })
    key = "bb.j2.j22.j0"
    d = get_data_value(data,key)
    print(d)