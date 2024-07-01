import pandas as pd
from sqlalchemy import create_engine
import configparser


def read_db_config(filename=r'D:\豆瓣电影分析\项目\utils\config.ini', section='database'):
    """
    读取数据库配置信息
    :param filename:配置文件名
    :param section:配置文件中的section名
    :return:数据库配置字典
    """
    parser = configparser.ConfigParser()
    parser.read(filename)

    db_config = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db_config[item[0]] = item[1]
    else:
        raise Exception(f"{section} not found in {filename} file")

    return db_config


db_config = read_db_config()

# 创建数据库连接字符串
db_url = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['db_name']}?charset={db_config['charset']}"

con = create_engine(db_url)
df = pd.read_sql('select * from movie_data', con=con)

def typelist(col_name):
    types = df[col_name].values
    types = list(map(lambda x: x.split('、'), types))
    type_list = []
    for i in types:
        for j in i:
            type_list.append(j)

    return type_list


def countrylist(col_name):
    types = df[col_name].values
    types = list(map(lambda x: x.split('/'), types))
    type_list = []
    for i in types:
        for j in i:
            j = j.strip()
            type_list.append(j)

    return type_list
