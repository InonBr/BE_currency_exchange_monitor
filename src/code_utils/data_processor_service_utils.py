from db import upload_to_db


def convert_dic_to_list(dic):
    list_of_dic = [{key: value} for key, value in dic.items()]
    list_of_dic = create_mongo_dic(list_of_dic)

    upload_to_db(list_of_dic)


def create_mongo_dic(list_of_dic):
    for dic in list_of_dic:
        dic["name"] = list(dic.keys())[0]
        dic["value"] = dic[dic["name"]]
        del dic[dic["name"]]

    return list_of_dic
