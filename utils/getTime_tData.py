import re

from .utils import *


def getYearData():
    df1 = pd.DataFrame([])
    # df['years'] = df['years'].replace('未知', '2005')
    df1['years'] = df['years'].replace('未知', '2005').map(lambda x: int(x[:4]))
    df1['score'] = df['score'].map(lambda x: float(x))
    new_list = df1['years'].values
    new_list.sort()
    print(new_list)
    # time_list = df['years'].values
    # new_list = []
    # for i in time_list:
    #     i = int(i[:4])
    #     new_list.append(i)
    # new_list.sort()
    timeObj = {}
    for i in new_list:
        if timeObj.get(i, -1) == -1:
            timeObj[i] = 1
        else:
            timeObj[i] = timeObj[i] + 1
    return list(timeObj.keys()), list(timeObj.values())


def getMovieTimeData():
    movietime = df['times'].values
    movieList = []
    for i in movietime:
        i = i.split('分')[0]
        numbers = re.findall(r'\d+', i)
        for j in numbers:
            movieList.append(int(j))
    movieTimeData = [{
        'name': '短',
        'value': 0
    }, {
        'name': '中',
        'value': 0
    }, {
        'name': '长',
        'value': 0
    }, {
        'name': '特长',
        'value': 0
    }]
    for i in movieList:
        if i <= 60:
            movieTimeData[0]['value'] = movieTimeData[0]['value'] + 1
        elif i <= 120:
            movieTimeData[1]['value'] = movieTimeData[1]['value'] + 1
        elif i <= 150:
            movieTimeData[2]['value'] = movieTimeData[2]['value'] + 1
        else:
            movieTimeData[3]['value'] = movieTimeData[3]['value'] + 1
    return movieTimeData
