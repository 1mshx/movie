from .utils import *


def getTypeData():
    typeList = typelist('types')
    typeObj = {}
    for i in typeList:
        if typeObj.get(i, -1) == -1:
            typeObj[i] = 1
        else:
            typeObj[i] = typeObj[i] + 1
    type_List = []
    for i in range(20):
        type_List.append(
            {'value': list(typeObj.values())[i], 'name': list(typeObj.keys())[i]})
    return type_List
