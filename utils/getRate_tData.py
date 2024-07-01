from .utils import *


def getAllTypes():
    return list(set(typelist('types')))


def getAllRateDataByType(type):
    global rateList
    if type == 'all':
        rateList = df['score'].map(lambda x: float(x)).values
    else:
        typeList = df['types'].map(lambda x: x.split('、')).values
        ordrateList = df['score'].map(lambda x: float(x)).values
        rateList = []
        for i, item in enumerate(typeList):
            if type in item:
                rateList.append(ordrateList[i])
    rateList.sort()
    rateObj = {}
    for i in rateList:
        if rateObj.get(i, -1) == -1:
            rateObj[i] = 1
        else:
            rateObj[i] = rateObj[i] + 1
    return list(rateObj.keys()), list(rateObj.values())


def getStart(searchIpt):
    tableData = df.values
    resuleData = []
    for i in tableData:
        if i[3].find(searchIpt) != -1:
            resuleData.append(i)

    if len(resuleData) == 0:
        searchIpt = "霸王别姬"
    else:
        searchIpt = searchIpt

    starts_five = list(df.loc[df['namess'].str.contains(searchIpt)]['five'])[0]
    starts_four = list(df.loc[df['namess'].str.contains(searchIpt)]['four'])[0]
    starts_three = list(df.loc[df['namess'].str.contains(searchIpt)]['three'])[0]
    starts_two = list(df.loc[df['namess'].str.contains(searchIpt)]['two'])[0]
    starts_one = list(df.loc[df['namess'].str.contains(searchIpt)]['one'])[0]
    searchName = list(df.loc[df['namess'].str.contains(searchIpt)]['namess'])[0]
    startsData = [{
        'name': '五星',
        'value': "{:.2f}".format(float(starts_five) * 100)
    }, {
        'name': '四星',
        'value': "{:.2f}".format(float(starts_four) * 100)
    }, {
        'name': '三星',
        'value': "{:.2f}".format(float(starts_three) * 100)
    }, {
        'name': '二星',
        'value': "{:.2f}".format(float(starts_two) * 100)
    }, {
        'name': '一星',
        'value': "{:.2f}".format(float(starts_one) * 100)
    }]
    return startsData, searchName


def getYearMeanData():
    df1 = pd.DataFrame([])
    df1['years'] = df['years'].replace('未知', '2005').map(lambda x: int(x[:4]))
    df1['score'] = df['score'].map(lambda x: float(x))
    yearList = df1['years'].values
    yearList.sort()
    yearList = list(set(yearList))
    meanList = []
    for i in yearList:
        a = "{:.2f}".format(float(df1[df1['years'] == i]['score'].mean()))
        meanList.append(float(a))
    return yearList, meanList
