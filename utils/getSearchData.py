from .getHomeData import gettrailer
from .utils import *


def getMovieDetailById(movieName):
    tableData = df.values
    resuleData = []
    for i in tableData:
        if i[3] == movieName:
            i[20] = eval(i[20])
            resuleData.append(i)
    return resuleData


def getMovieDetailBySearchWord(searchword):
    tableData = df.values
    resuleData = []
    for i in tableData:
        if i[3].find(searchword) != -1:
            i[20] = eval(i[20])
            resuleData.append(i)
    return resuleData
