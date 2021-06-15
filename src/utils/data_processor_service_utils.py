import uuid


def convert_dic_to_list(dic):
    list_of_dic = [{key: value} for key, value in dic.items()]
    list_of_dic = create_mongo_dic(list_of_dic)

    print(list_of_dic)


def create_mongo_dic(list_of_dic):
    for dic in list_of_dic:
        dic["name"] = list(dic.keys())[0]
        dic["value"] = dic[dic["name"]]
        dic["_id"] = uuid.uuid4().hex
        del dic[dic["name"]]

    return list_of_dic
