from .utils import *


def getMapData():
    mapList = countrylist('country')
    mapObj = {}
    for i in mapList:
        if mapObj.get(i, -1) == -1:
            mapObj[i] = 1
        else:
            mapObj[i] = mapObj[i] + 1
    return list(mapObj.keys()), list(mapObj.values())


def getLangData():
    langList = countrylist('languages')
    langObj = {}
    for i in langList:
        if langObj.get(i, -1) == -1:
            langObj[i] = 1
        else:
            langObj[i] = langObj[i] + 1
    sorted_data = dict(sorted(langObj.items(), key=lambda item: item[1], reverse=True))
    lang_list = []
    for i in range(20):
        lang_list.append(
            {'value': list(sorted_data.values())[i], 'name': list(sorted_data.keys())[i]})

    return list(langObj.keys()), list(langObj.values()), lang_list
