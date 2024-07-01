from flask import Flask, render_template, request, session, redirect
from utils import query
from utils.getHomeData import *
from utils.getMapData import *
from utils.getSearchData import *
from utils.getTime_tData import *
from utils.getRate_tData import *
from utils.getType_tData import *
from utils.getActor_tData import *
from utils.getTableData import *
from world_cloud import *
from utils.getComments_cData import *
from utils.getPredictData import *

app = Flask(__name__)
app.secret_key = "This is session_key you know ?"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        request.form = dict(request.form)

        def filter_fn(item):
            return request.form['email'] in item and request.form['password'] in item

        users = query.querys('select * from users', [], 'select')
        filter_user = list(filter(filter_fn, users))

        if len(filter_user):
            session['email'] = request.form['email']
            return redirect('/home')
        else:
            return render_template('error.html', message='邮箱或者密码错误')


@app.route('/loginOut')
def loginOut():
    session.clear()
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        request.form = dict(request.form)
        if request.form['password'] != request.form['passwordChecked']:
            return render_template('error.html', message='两次输入密码不相同')

        def filter_fn(item):
            return request.form['email'] in item

        users = query.querys('select * from users', [], 'select')
        filter_list = list(filter(filter_fn, users))
        if len(filter_list):
            return render_template('error.html', message='该用户已注册')
        else:
            query.querys('insert into users(email, password) values (%s, %s)',
                         [request.form['email'], request.form['password']])
            return redirect('/home')


@app.route('/', methods=['GET', 'POST'])
def allRequest():
    return redirect('/login')


@app.before_request
def before_request():
    pat = re.compile(r'^/static')
    if re.search(pat, request.path):
        return
    if request.path == '/login':
        return
    if request.path == '/register':
        return
    email = session.get('email')
    if email:
        return None
    return redirect('/login')


@app.route('/home', methods=['GET', 'POST'])
def home():
    email = session.get('email')
    maxMovieLen, maxscore, maxActors, maxCountry, types, maxLanguage = getHomeData()
    typeEcharData = getTypeEchardata()
    row, col = getRateEcharData()
    tableData = getTableData()
    return render_template(
        'index.html',
        email=email,
        maxMovieLen=maxMovieLen,
        maxscore=maxscore,
        maxActors=maxActors,
        maxCountry=maxCountry,
        types=types,
        maxLanguage=maxLanguage,
        typeEcharData=typeEcharData,
        row=row,
        col=col,
        tableData=tableData

    )


@app.route('/movie/<movieName>')
def movie(movieName):
    movieUrl = getMovieUrlById(movieName)
    return render_template('movie.html', movieUrl=movieUrl)


@app.route('/search/<movieName>', methods=['GET', 'POST'])
def search(movieName):
    email = session.get('email')
    if request.method == 'GET':
        resultData = getMovieDetailById(movieName)
    else:
        request.form = dict(request.form)
        resultData = getMovieDetailBySearchWord(request.form['searchWord'])
    types = len(resultData)
    return render_template('search.html', resultData=resultData, email=email, types=types)


@app.route('/time_t')
def time_t():
    email = session.get('email')
    row, col = getYearData()
    movieTimeData = getMovieTimeData()
    return render_template('time_t.html', email=email, row=row, col=col, movieTimeData=movieTimeData)


@app.route('/rate_t/<type>', methods=['GET', 'POST'])
def rate_t(type):
    email = session.get('email')
    typeList = getAllTypes()
    row, col = getAllRateDataByType(type)
    if request.method == 'GET':
        startsData, searchName = getStart('霸王别姬')
    else:
        request.form = dict(request.form)
        startsData, searchName = getStart(request.form['searchIpt'])
        if len(searchName) == 0:
            startsData, searchName = getStart('霸王别姬')

    yearMeanRow, yearMeanCol = getYearMeanData()

    return render_template('rate_t.html', email=email, typeList=typeList,
                           type=type, row=row, col=col, startsData=startsData, searchName=searchName,
                           yearMeanRow=yearMeanRow, yearMeanCol=yearMeanCol)


@app.route('/map_t')
def map_t():
    email = session.get('email')
    row, col = getMapData()
    langrow, langcol, langdict = getLangData()
    return render_template('map_t.html', email=email, row=row, col=col,
                           langrow=langrow, langcol=langcol, langdict=langdict)


@app.route('/type_t')
def type_t():
    email = session.get('email')
    type_List = getTypeData()
    return render_template('type_t.html', email=email, type_List=type_List)


@app.route('/actor_t')
def actor_t():
    email = session.get('email')
    derected_row, derected_col = getDerected()
    actors_row, actors_col = getCastsDataTop20()
    return render_template('actor_t.html', email=email, derected_row=derected_row,
                           derected_col=derected_col, actors_row=actors_row, actors_col=actors_col)


@app.route('/table/<movieName>/<uid>')
def table(movieName, uid):
    email = session.get('email')
    print(movieName, uid)
    tableData = getTableDataPage()
    if movieName != '0' and email == "2801417588@qq.com":
        delMovieByMovieName(movieName,uid)
        return redirect('/table/0/0')
    return render_template('table.html', email=email, tableData=tableData)


@app.route('/comments_c', methods=['GET', 'POST'])
def comments_c():
    email = session.get('email')
    if request.method == 'GET':
        return render_template('comments_c.html', email=email)
    else:
        resSrc, searchName = getCommentsImage(dict(request.form)['searchIpt'])
        return render_template('comments_c.html', email=email, resSrc=resSrc, searchName=searchName)


@app.route('/title_c')
def title_c():
    email = session.get('email')
    return render_template('title_c.html', email=email)


@app.route('/casts_c')
def casts_c():
    email = session.get('email')
    return render_template('casts_c.html', email=email)


@app.route('/summary_c')
def summary_c():
    email = session.get('email')
    return render_template('summary_c.html', email=email)


@app.route('/pred')
def pred():
    email = session.get('email')
    predData = getPredictData()
    return render_template('predict.html', email=email, predData=predData)


if __name__ == '__main__':
    app.run(debug=True)
