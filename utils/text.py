# # import pandas as pd
# # import numpy as np
# # import re
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # from pyecharts.charts import Bar
# # from pyecharts import options as opts
# # from pyecharts.render import make_snapshot
# # from snapshot_selenium import snapshot
# #
# # df = pd.read_csv(r'D:\豆瓣电影分析\爬虫\tempData1.csv', na_values=['[]', 0])
# # df = df.drop_duplicates()
# #
# # # 删除不要的列
# # df.drop(['url', 'cover', 'pictureurl', 'trailer'], axis=1, inplace=True)
# # # 对于director列中存在缺失值直接删除整行
# # df.dropna(subset=['director'], inplace=True)
# # # 对于年份和简介的缺失值直接用特定值代替
# # df['years'].fillna("['2005']", inplace=True)
# # df['plot'].fillna("['无简介']", inplace=True)
# # # 对于评分占比缺失值直接用0代替
# # df['one'].fillna(0, inplace=True)
# # df['two'].fillna(0, inplace=True)
# # # 对于编剧缺失值直接用导演代替
# # df['screenwriter'] = df['screenwriter'].fillna(df['director'])
# # # 重新编辑索引
# # df.reset_index(drop=True, inplace=True)
# #
# # # 对数据进行处理
# # df['director'] = df['director'].apply(lambda x: eval(x))
# # df['screenwriter'] = df['screenwriter'].apply(lambda x: eval(x))
# # df['actors'] = df['actors'].apply(lambda x: eval(x))
# # df['types'] = df['types'].apply(lambda x: eval(x))
# # df['country'] = df['country'].apply(lambda x: x.split('/'))
# # df['country'] = df['country'].apply(lambda x: [genre.strip() for genre in x])
# # df['languages'] = df['languages'].apply(lambda x: x.split('/'))
# # df['languages'] = df['languages'].apply(lambda x: [genre.strip() for genre in x])
# # df['years'] = df['years'].map(lambda x: eval(x)[0][:4])
# # df['times'] = df['times'].map(lambda x: re.findall(r'\d+', x.split('分')[0]))
# # df['times'] = df['times'].apply(lambda x: x[0] if x else None)
# # df['plot'] = df['plot'].apply(lambda x: eval(x)[0])
# # df['review'] = df['review'].apply(lambda x: eval(x))
# #
# # df.dropna(subset=['times'], inplace=True)
# # df.reset_index(drop=True, inplace=True)
# #
# # df_type = df['country']
# # all_genres = [genre for sublist in df_type for genre in sublist]
# #
# # # # 统计各个类型的数量
# # genre_counts = pd.Series(all_genres).value_counts()
# #
# # bar_chart = Bar()
# #
# # # 添加 x 轴和 y 轴的数据
# # bar_chart.add_xaxis(list(genre_counts.index)[:10])
# # bar_chart.add_yaxis('电影数量', genre_counts.to_list()[:10])
# #
# # # 设置图表的标题和坐标轴标签
# # bar_chart.set_global_opts(title_opts=opts.TitleOpts(title='地区类型统计', pos_top='100%', pos_left='50%'),
# #                           xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
# #                           yaxis_opts=opts.AxisOpts(name='数量'))
# #
# # # 渲染并保存或显示图表
# # bar_chart.render('area_chart.html')
#
#
# import re
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from nltk.corpus import stopwords
# from textblob import TextBlob
#
# # 简介数据
# summaries = [
#     '段小楼（张丰毅）与程蝶衣（张国荣）是一对打小一起长大的师兄弟，两人一个演生，一个饰旦，一向配合天衣无缝，尤其一出《霸王别姬》，更是誉满京城，为此，两人约定合演一辈子《霸王别姬》。但两人对戏剧与人生关系的理解有本质不同，段小楼深知戏非人生，程蝶衣则是人戏不分。',
#     '伦敦著名刑案辩护律师韦菲爵士（查尔斯•劳顿 Charles Laughton 饰）接受了心脏病治疗，但是身体依旧虚弱，第一天回家休养，护士一直严厉监督他服药，并杜绝烟酒。管家为了便于上楼，还专门为他修了电梯。但是，种种关心照顾，对于这位桀骜不驯、牙尖嘴利的大律师根本不起作用，反倒是一纸诉状令他倍感兴奋。律师梅休和当事人沃尔（泰隆•鲍华 Tyrone Power饰）登门拜访，请他出山打官司。原来，沃尔结识了富婆，两人相见甚欢，虽然仆人对他发明的打蛋器充满鄙夷，但是富婆却对他充满爱意，甚至为他修改了遗嘱，把8万英镑留给了他。然而，富婆却惨遭毒手。于是，沃尔成为警方的头号嫌疑犯。他的唯一证人是妻子克里斯汀（玛琳•黛德丽 Marlene Dietrich饰），然而后者登门时的冷漠与淡定，令韦菲爵士怀疑这其中另有隐情。在扑朔迷离的案件背后，隐藏着一个个环环相扣...',
#     '1912年4月10日，号称 “世界工业史上的奇迹”的豪华客轮泰坦尼克号开始了自己的处女航，从英国的南安普顿出发驶往美国纽约。富家少女罗丝（凯特•温丝莱特）与母亲及未婚夫卡尔坐上了头等舱；另一边，放荡不羁的少年画家杰克（莱昂纳多·迪卡普里奥）也在码头的一场赌博中赢得了下等舱的船票。罗丝厌倦了上流社会虚伪的生活，不愿嫁给卡尔，打算投海自尽，被杰克救起。很快，美丽活泼的罗丝与英俊开朗的杰克相爱，杰克带罗丝参加下等舱的舞会、为她画像，二人的感情逐渐升温。',
#     '阿甘（汤姆·汉克斯 饰）于二战结束后不久出生在美国南方阿拉巴马州一个闭塞的小镇，他先天弱智，智商只有75，然而他的妈妈是一个性格坚强的女性，她常常鼓励阿甘“傻人有傻福”，要他自强不息。阿甘像普通孩子一样上学，并且认识了一生的朋友和至爱珍妮（罗宾·莱特·潘 饰），在珍妮 和妈妈的爱护下，阿甘凭着上帝赐予的“飞毛腿”开始了一生不停的奔跑。阿甘成为橄榄球巨星、越战英雄、乒乓球外交使者、亿万富翁，但是，他始终忘不了珍妮，几次匆匆的相聚和离别，更是加深了阿甘的思念。',
#     '犹太青年圭多（罗伯托·贝尼尼）邂逅美丽的女教师多拉（尼可莱塔·布拉斯基），他彬彬有礼的向多拉鞠躬：“早安！公主！”。历经诸多令人啼笑皆非的周折后，天遂人愿，两人幸福美满的生活在一起。然而好景不长，法西斯政权下，圭多和儿子被强行送往犹太人集中营。多拉虽没有犹太血统，毅然同行，与丈夫儿子分开关押在一个集中营里。聪明乐天的圭多哄骗儿子这只是一场游戏，奖品就是一辆大坦克，儿子快乐、天真的生活在纳粹的阴霾之中。尽管集中营的生活艰苦寂寞，圭多仍然带给他人很多快乐，他还趁机在纳粹的广播里问候妻子：“早安！公主！”',
#     '1939年，波兰在纳粹德国的统治下，党卫军对犹太人进行了隔离统治。德国商人奥斯卡·辛德勒（连姆·尼森 Liam Neeson 饰）来到德军统治下的克拉科夫，开设了一间搪瓷厂，生产军需用品。凭着出众的社交能力和大量的金钱，辛德勒和德军建立了良好的关系，他的工厂雇用犹太人工作，大发战争财。1943年，克拉科夫的犹太人遭到了惨绝人寰的大屠杀，辛德勒目睹这一切，受到了极大的震撼，他贿赂军官，让自己的工厂成为集中营的附属劳役营，在那些疯狂屠杀的日子里，他的工厂也成为了犹太人的避难所。1944年，德国战败前夕，屠杀犹太人的行动越发疯狂，辛德勒向德军军官开出了1200人的名单，倾家荡产买下了这些犹太人的生命。在那些暗无天日的岁月里，拯救一个人，就是拯救全世界。',
#     '世纪之交，古老的中国正迎来前所未有的巨大变革。老态龙钟的大清王朝摇摇欲坠，六君子的鲜血无法阻止历史车轮的滚动，老北京城的上空风云变幻，波谲云诡。王利发（于是之 饰），北京城内裕泰茶馆的年轻掌柜。他谨记父亲的教诲，体面周全地迎送四方宾客。小小的茶馆内，三教九流各色人等穿梭于此：提笼架鸟哀叹时运的松二爷（黄宗洛 饰）；慨叹国之将亡的刚毅满人常四爷（郑榕 饰）；一心谋求实业救国的秦仲义（蓝天野 饰）；丧尽天良买卖人口的刘麻子（英若诚 饰）；打算娶老婆的庞太监（童超 饰）……你方唱罢我登场，小小茶馆之内演尽世间的沧桑与凄凉……',
#     '里昂（让·雷诺饰）是名孤独的职业杀手，受人雇佣。一天，邻居家小姑娘马蒂尔达（纳塔丽·波特曼饰)敲开他的房门，要求在他那里暂避杀身之祸。原来邻居家的主人是警方缉毒组的眼线，只因贪污了一小包毒品而遭恶警（加里·奥德曼饰）杀害全家的惩罚。马蒂尔达得到里昂的留救，幸免于难，并留在里昂那里。里昂教小女孩使枪，她教里昂法文，两人关系日趋亲密，相处融洽。女孩想着去报仇，反倒被抓，里昂及时赶到，将女孩救回。混杂着哀怨情仇的正邪之战渐次升级，更大的冲突在所难免……'
# ]
#
# # 定义停用词
# stop_words = set(stopwords.words('english'))
#
#
# # 文本清洗和分词
# def clean_text(text):
#     # 去除特殊字符和数字
#     text = re.sub(r'[^a-zA-Z\s]', '', text)
#     # 转换为小写
#     text = text.lower()
#     # 分词
#     words = text.split()
#     # 去除停用词
#     words = [word for word in words if word not in stop_words]
#     return ' '.join(words)
#
#
# # 清洗文本
# cleaned_summaries = [clean_text(summary) for summary in summaries]
#
#
# def cidai(data):
#     # 创建词袋模型表示
#     count_vectorizer = CountVectorizer()
#     count_matrix = count_vectorizer.fit_transform(data)
#     # return count_matrix
#     #
#     # # 创建TF-IDF向量化
#     tfidf_vectorizer = TfidfVectorizer()
#     tfidf_matrix = tfidf_vectorizer.fit_transform(data)
#     return tfidf_matrix
#     # # 输出特征维度
#     # print("词袋模型特征维度:", count_matrix.shape)
#     #
#     # print("TF-IDF特征维度:", tfidf_matrix)
#
#
# cidai_matrix = cidai(cleaned_summaries)
# print(cidai_matrix)

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Define the flowchart steps
steps = [
    {"name": "收集URL地址", "position": (0.5, 0.85)},
    {"name": "发送请求", "position": (0.5, 0.7)},
    {"name": "获取响应", "position": (0.5, 0.55)},
    {"name": "解析和提取数据", "position": (0.5, 0.4)},
    {"name": "处理和存储数据", "position": (0.5, 0.25)},
    {"name": "继续获取新的URL地址", "position": (0.5, 0.1)}
]

# Draw the flowchart
for step in steps:
    ax.text(step["position"][0], step["position"][1], step["name"],
            ha="center", va="center", fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

# Draw arrows between steps
for i in range(len(steps) - 1):
    ax.annotate("", xy=steps[i + 1]["position"], xytext=steps[i]["position"],
                arrowprops=dict(arrowstyle="->", color="black"))

# Loop arrow from the last step to the first
ax.annotate("", xy=(0.5, 0.9), xytext=(0.5, 0.15),
            arrowprops=dict(arrowstyle="-|>", color="black", linestyle="--"))

# Hide axes
ax.set_axis_off()

# Display the flowchart
plt.show()
