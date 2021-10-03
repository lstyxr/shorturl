from flask import Flask, render_template, request
import pymysql
from werkzeug.utils import redirect
import bases

host = 'http://127.0.0.1:5000/'

try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='shorturl',
        charset='utf8'
    )
except pymysql.Error:
    raise

cursor = connection.cursor()

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gen_short_url/', methods=["POST"])
def gen_short_url():
    long_url = request.form.get('long_url')
    # 将长链接（实际链接存入数据库）
    try:
        cursor.execute('insert into urls (url) values ("{}")'.format(long_url))  # 插入语句使用了字符串拼接
        connection.commit()
    except pymysql.Error:
        raise

    # 获取 ID
    last_id = cursor.lastrowid
    # 转换进制
    encode = bases.base62_encode(last_id)
    short_url = host + encode
    return render_template('index.html', short_url=short_url)

@app.route('/<encode_id>')
def redirect_url(encode_id):
    id = bases.base62_decode(encode_id)
    try:
        cursor.execute('select url from urls where id= {}'.format(id))
        connection.commit()
        url = cursor.fetchone()
        return redirect(url[0])
    except pymysql.Error:
        raise