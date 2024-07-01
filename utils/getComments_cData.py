from .utils import *
import json
import sys

sys.path.append('..')
from world_cloud import *


def getCommentsImage(searchIpt):
    tableData = df.values
    resuleData = []
    for i in tableData:
        if i[3].find(searchIpt) != -1:
            resuleData.append(i)
    if len(resuleData) == 0:
        searchIpt = "霸王别姬"
    else:
        searchIpt = searchIpt
    searchName = list(df.loc[df['namess'].str.contains(searchIpt)]['namess'])[0]
    comments = df[df['namess'] == searchName]['review'].values[0]
    comments = json.loads(comments)
    resSrc = getImageByComments(comments)
    return resSrc, searchName
