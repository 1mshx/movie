from .utils import *


def getDerected():
    derectedlist = countrylist('director')
    derectedObj = {}
    for i in derectedlist:
        if derectedObj.get(i, -1) == -1:
            derectedObj[i] = 1
        else:
            derectedObj[i] = derectedObj[i] + 1
    sorted_data = dict(sorted(derectedObj.items(), key=lambda item: item[1]))
    print(sorted_data)

    return list(sorted_data.keys())[-20:], list(sorted_data.values())[-20:]


def getCastsDataTop20():
    actorslist = typelist('actors')
    actorsObj = {}
    for i in actorslist:
        if actorsObj.get(i, -1) == -1:
            actorsObj[i] = 1
        else:
            actorsObj[i] = actorsObj[i] + 1
    sorted_data = dict(sorted(actorsObj.items(), key=lambda item: item[1]))

    return list(sorted_data.keys())[-20:], list(sorted_data.values())[-20:]
