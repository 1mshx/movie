from .query import querys
from .utils import *


def delMovieByMovieName(movieName,uid):
    sql = "DELETE FROM movie_data WHERE namess = %s"
    sql1 = "DELETE FROM pred_data WHERE id1 = %s"
    querys(sql, [movieName])
    querys(sql1, [uid])
    return "删除成功"


def getTableDataPage():
    da = pd.read_sql('select * from movie_data', con=con)
    data = da.values
    for i, item in enumerate(data):
        item[2] = eval(item[2])[0]
        item[20] = eval(item[20])
    return data
