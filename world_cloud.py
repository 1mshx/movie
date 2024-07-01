import jieba
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import random
from utils.query import querys
from utils.utils import typelist


def getImageByComments(comments):
    text = ''
    for i in comments:
        text = text + i['content']

    # 分词
    cut = jieba.cut(text)
    string = ' '.join(cut)

    img = Image.open('./static/img/1.png')
    img_arr = np.array(img)
    wc = WordCloud(
        background_color='white',
        mask=img_arr,
        font_path='STHUPO.TTF'
    )
    wc.generate_from_text(string)

    # 绘制图片
    flg = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')

    randomInt = random.randint(1, 100000000)
    plt.savefig(f'./static/cyt/{randomInt}.png')

    return f'./static/cyt/{randomInt}.png'


def getImageByAuthor(field, targetImage, resImage):
    # 停用词列表，你可以根据需要添加或删除停用词
    stopwords = {'是', '的', '在', '与', '一', '他', '她', '和', '他们', '她们', '被', '了', '但', '到', '却', '到',
                 '然而'}

    sql = 'select {} from movie_data'.format(field)
    data = querys(sql, [], 'select')
    text = ''
    for i in data:
        text = text + i[0]

    # 分词
    cut = jieba.cut(text)
    string = ' '.join([word for word in cut if word not in stopwords])

    img = Image.open(targetImage)
    img_arr = np.array(img)
    wc = WordCloud(
        background_color='white',
        mask=img_arr,
        font_path='STHUPO.TTF'
    )
    wc.generate_from_text(string)

    # 绘制图片
    flg = plt.figure(1)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')

    randomInt = random.randint(1, 100000000)
    plt.savefig(resImage)


# getImageByAuthor('plot', './static/img/3.png', './static/img/summary_cloud.png')

def getImageByCasts(targetImage, resImage):
    castsList = typelist('actors')
    text = ''
    for i in castsList:
        text = text + i

    # 分词
    cut = jieba.cut(text)
    string = ' '.join(cut)

    img = Image.open(targetImage)
    img_arr = np.array(img)
    wc = WordCloud(
        background_color='white',
        mask=img_arr,
        font_path='STHUPO.TTF'
    )
    wc.generate_from_text(string)

    # 绘制图片
    flg = plt.figure(1)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')

    plt.savefig(resImage)


getImageByCasts('./static/img/4.png', './static/img/casts_cloud.png')
