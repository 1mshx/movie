import re
from time import sleep
import pandas as pd
from pymysql import cursors
from pymysql import *
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
conn = connect(host=db_config['host'],
               port=int(db_config['port']),
               user=db_config['user'],
               passwd=db_config['password'],
               db=db_config['db_name'],
               charset=db_config['charset'])
cursor = conn.cursor()


def create_table():
    """
    连接数据库，创建movie表
    :return:
    """
    db_config = read_db_config()
    try:
        conn = connect(host=db_config['host'],
                       port=int(db_config['port']),
                       user=db_config['user'],
                       passwd=db_config['password'],
                       db=db_config['db_name'],
                       charset=db_config['charset'])
        sql = '''
                CREATE TABLE IF NOT EXISTS movie_data(
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            url VARCHAR(255),
                            cover VARCHAR(255),
                            namess VARCHAR(255),
                            director VARCHAR(255),
                            screenwriter VARCHAR(255),
                            actors VARCHAR(2555),
                            types VARCHAR(255),
                            country VARCHAR(255),
                            languages VARCHAR(255),
                            years VARCHAR(255),
                            times VARCHAR(255),
                            plot text,
                            score VARCHAR(255),
                            numbers VARCHAR(255),
                            five VARCHAR(255),
                            four VARCHAR(255),
                            three VARCHAR(255),
                            two VARCHAR(255),
                            one VARCHAR(255),
                            pictureurl VARCHAR(2555),
                            review text,
                            trailer VARCHAR(2555)
                        );        
            '''

        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("表创建成功")
    except MySQLError as e:
        print(f"数据库错误：{e}")
    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        if conn:
            conn.close()

def create_table1():
    """
    连接数据库，创建movie表
    :return:
    """
    db_config = read_db_config()
    try:
        conn = connect(host=db_config['host'],
                       port=int(db_config['port']),
                       user=db_config['user'],
                       passwd=db_config['password'],
                       db=db_config['db_name'],
                       charset=db_config['charset'])
        sql = '''
                CREATE TABLE IF NOT EXISTS pred_data(
                            id1 INT PRIMARY KEY AUTO_INCREMENT,
                            director1 float,
                            screenwriter1 float,
                            actors1 float,
                            types1 float,
                            country1 float,
                            languages1 float,
                            years1 float,
                            times1 float,
                            score1 float,
                            numbers1 float,
                            five1 float,
                            four1 float,
                            three1 float,
                            two1 float,
                            one1 float,
                            review1 float,
                            new_review1 float,
                            piaofang1 float,
                            predictions float
                        );        
            '''

        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("表创建成功")
    except MySQLError as e:
        print(f"数据库错误：{e}")
    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        if conn:
            conn.close()


def querys(sql, params, type='no_select'):
    params = tuple(params)
    cursor.execute(sql, params)
    if type != 'no_select':
        data_list = cursor.fetchall()
        conn.commit()
        return data_list
    else:
        conn.commit()
        return "数据库语句执行成功"
