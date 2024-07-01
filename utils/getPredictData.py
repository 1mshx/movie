from .utils import *


def getPredictData():
    data = pd.read_sql('select * from movie_data', con=con)
    data1 = pd.read_sql('select * from pred_data', con=con)
    pred_data = pd.concat([data, data1.iloc[:, -2:]], axis=1).values
    print(pred_data)
    return pred_data
