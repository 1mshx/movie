from lxml import etree

import pandas as pd
import requests

from .utils import *


def getData():
    maxMovieLen = len(df)  # 电影总个数
    maxscore = df['score'].max()  # 电影最高评分
    actors_list = typelist('actors')
    maxActors = max(actors_list, key=actors_list.count)  # 最多演员出场
    country_list = countrylist('country')
    maxCountry = max(country_list, key=country_list.count)  # 制片国家最多数
    types_list = typelist('types')
    types = len(set(types_list))  # 电影种类数
    languages_list = countrylist('languages')
    maxLanguage = max(languages_list, key=languages_list.count)  # 最多语言
    data_list = [maxMovieLen, maxscore, maxActors, maxCountry, types, maxLanguage]
    data_frame = pd.DataFrame([data_list],
                              columns=['maxMovieLen', 'maxscore', 'maxActors', 'maxCountry', 'types', 'maxLanguage'])
    data_frame.to_csv('HomeData.csv', index=False)


def getHomeData():
    df = pd.read_csv(r'D:\豆瓣电影分析\项目\utils\HomeData.csv', encoding='utf-8')
    maxMovieLen = df['maxMovieLen'][0]
    maxscore = df['maxscore'][0]
    maxActors = df['maxActors'][0]
    maxCountry = df['maxCountry'][0]
    types = df['types'][0]
    maxLanguage = df['maxLanguage'][0]

    return maxMovieLen, maxscore, maxActors, maxCountry, types, maxLanguage


def getTypeEchardata():
    types_list = typelist('types')
    typeObj = {}
    for i in types_list:
        if typeObj.get(i, -1) == -1:
            typeObj[i] = 1
        else:
            typeObj[i] = typeObj[i] + 1
    typeEcharData = []
    for key, value in typeObj.items():
        typeEcharData.append({
            'name': key,
            'value': value
        })
    return typeEcharData


def gettrailer(url):
    USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36")
    headers = {'User-Agent': USER_AGENT,
               'Referer': 'https://movie.douban.com/',
               'Cookie': 'bid=SJxhZK8sYWg; _pk_id.100001.4cf6=e8ac813cdadbcbd8.1711020150.; push_noty_num=0; '
                         'push_doumail_num=0; ll="118270"; __yadk_uid=KTOXv6uxqaBnnTKHrjJBQdiIyjS5sKQw; '
                         '_vwo_uuid_v2=DD06ECBCC29E3B4D12776B7BA243F882A|673fa97440b0c6cde1f443402079ceb9; '
                         '__utmv=30149280.27916; _ga=GA1.1.1663015970.1712235586; '
                         '_ga_Y4GN1R87RG=GS1.1.1712235586.1.1.1712235618.0.0.0; '
                         '__gads=ID=a72efd12384a73b2:T=1711583487:RT=1713363448:S=ALNI_Mb1SwwJOJ-nch9WTnnUaBYPF_g5wg; '
                         '__gpi=UID=00000d6e8e16c159:T=1711583487:RT=1713363448:S=ALNI_MZZbaBU7PzO3kL8wSybRIcJOc6DJQ; '
                         '__eoi=ID=10fe80fa551624b1:T=1711583487:RT=1713363448:S=AA-AfjZ5iFuLE3p6UgO9pncNSjjz; ct=y; '
                         '__utmc=30149280; __utmc=223695111; '
                         '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1713760110%2C%22http%3A%2F%2Flocalhost%3A8888%2F'
                         '%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,'
                         '6.0; __utma=30149280.1546699660.1711020150.1713760110.1713760403.32; '
                         '__utmb=30149280.0.10.1713760403; __utmz=30149280.1713760403.32.6.utmcsr=baidu|utmccn=('
                         'organic)|utmcmd=organic; __utma=223695111.26169246.1711020150.1713760110.1713760403.32; '
                         '__utmb=223695111.0.10.1713760403; __utmz=223695111.1713760403.32.6.utmcsr=baidu|utmccn=('
                         'organic)|utmcmd=organic; dbcl2="279161465:eOHmmLc4Ujo"; ck=Qslk'
               }

    # 发送请求
    response = requests.get(url=url, headers=headers)

    # 解析网页
    content = response.text
    a = etree.HTML(content)

    data = []

    # 预告片地址
    try:
        ygp_url = a.xpath('//*[@id="related-pic"]/ul/li[@class="label-trailer"]/a/@href')
        ygpHTML = requests.get(url=ygp_url[0], headers=headers)
        ygpXPATH = etree.HTML(ygpHTML.text)
        movieurl = ygpXPATH.xpath('//video/source/@src')
        data.append(movieurl[0])
    except:
        data.append(0)
    return data


def getRateEcharData():
    ratelist = df['score'].map(lambda x: float(x)).values
    ratelist.sort()
    rateObj = {}
    for i in ratelist:
        if rateObj.get(i, -1) == -1:
            rateObj[i] = 1
        else:
            rateObj[i] = rateObj[i] + 1
    return list(rateObj.keys()), list(rateObj.values())


def getTableData():
    tableData = df.values
    for i, item in enumerate(tableData):
        item[2] = eval(item[2])[0]
        item[4] = item[4].split('/')[0]
        item[20] = eval(item[20])
    return tableData


def getMovieUrlById(movieName):
    tableData = df
    url = tableData[tableData['namess'] == movieName].values[0][1]
    print(url)
    data = gettrailer(url)[0]
    return data
