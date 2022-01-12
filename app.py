<<<<<<< HEAD
# mongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
=======
# flask
from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)
>>>>>>> 05fac375bbfc5789ef3cd006685ccd4c44e73ca2

# mongo
from pymongo import MongoClient
<<<<<<< HEAD
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta



app = Flask(__name__)

SECRET_KEY = 'SPARTA'

client = MongoClient('mongodb://test:test@3.83.182.90', 27017)
db = client.jgati


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload["id"]})
        return render_template('list.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("relogin"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("relogin"))


@app.route('/relogin')
def relogin():
    return render_template('index.html')




# ------------------------------- 회원가입 페이지 로드 / lsm -------------------------------
## 회원가입 페이지
@app.route('/join')
def join_page():
    return render_template('join.html')

# ----------------list 페이지 이동 :  ASJ-----------------------------------
@app.route('/list')
def page_list():
    return render_template('list.html')


=======
#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@3.83.182.90', 27017)
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@3.83.182.90', 27017)
db = client.jgati

SECRET_KEY = 'SPARTA'

import requests
from bs4 import BeautifulSoup

import jwt
import datetime
import hashlib
from werkzeug.utils import secure_filename

from datetime import datetime, timedelta
>>>>>>> 05fac375bbfc5789ef3cd006685ccd4c44e73ca2

# ---------------------------------------------------popup route   //  cyj
@app.route('/popup')
def pop():
    return render_template('popup.html')


# ---------------------------------------------------------------------------------------------------------


# ----------------로그인 페이지 : 기능 ----------------------------------------------------------------------
# ----------------로그인 id/pw 작업 페이지:  ASJ-----------------------------------

@app.route("/api/login", methods=['POST'])
def login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pwd_give']

    find_id = db.user_info.find_one({'ID': id_receive, 'PWD': pw_receive})

    if (find_id == None):
        payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=6)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token.decode('utf-8')})

<<<<<<< HEAD
    else:
        return jsonify({'result': 'fail'})



# ----------------로그인 id/pw 작업 페이지:  ASJ-----------------------------------
"""
@app.route('', methods=['POST'])
def login():
    info_login = request.form['']
    db.jGATI.find({'id': info_login},{'_id':False})
    return jsonify({'msg': '로그인 완료'})
"""
=======

# ----------------페이지 관련 py code ----------------------------------------------------------------------
# ----------------index page 호출 -----------------------------------
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"ID": payload["id"]})
        return render_template('list.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("relogin"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("relogin"))

@app.route('/relogin')
def relogin():
    return render_template('index.html')


# ------------------------------- 회원가입 페이지 로드 / lsm -------------------------------
## 회원가입 페이지
@app.route('/joinGet')
def join_page():
   return render_template('join.html')

# ----------------list 페이지 이동 :  ASJ-----------------------------------
@app.route('/list')
def list_page():
    contents = list(db.write_info.find({}, {"_id": False}))
    return render_template("list.html", contents=contents)

# ---------------------------------------------------popup route   //  cyj
@app.route('/popup')
def pop():
    return render_template('popup.html')
#---------------------------------------------------------------------------------------------------------




# ----------------로그인 페이지 : 기능 ----------------------------------------------------------------------
# ----------------로그인 id/pw 작업 페이지:  ASJ-----------------------------------
## 로그인
@app.route('/api/login', methods=['POST'])
def login():
    id_receive = request.form['id']
    pw_receive = request.form['pw']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    find_user = db.user_info.find_one({'ID': id_receive, 'PWD': pw_hash})
    print("---------55555-----------")
    if find_user is not None:
        print("---------66666-----------")
        payload = {
         'id': id_receive,
         'exp': datetime.utcnow() + timedelta(seconds=20)  # 로그인 10분 유지
        }

        # ----------------토큰 생성 ----------------------------------------------------------------------
        ## 원본(잘못된 코드)
        # token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        ## 수정본
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        # ----------------------------------------------------------------------------------------------

        print("---------777777-----------")
        return jsonify({'result': 'success', 'token': token.decode('utf-8'), 's_msg': '아이디/비밀번호가 맞습니다.'})
        # return jsonify({'result': 'success',  's_msg': '아이디/비밀번호가 맞습니다.'})
    else:
        return jsonify({'result': 'fail', 'f_msg': '아이디/비밀번호가 일치하지 않습니다.'})





# ---------------- 회원가입 페이지 : 기능 ----------------------------------------------------------------------
# ------------------------------- 회원가입 api / lsm -------------------------------
## 회원가입
@app.route('/api/membership', methods=['POST'])
def membership():
    id_receive = request.form['id_give']
    pw_receive = request.form['pwd_give']
    confirm_pwd_receive = request.form['confirm_pwd_give']
    email_receive = request.form['email_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    """
    ## 패스워드 confirm 로직 미완성 
        if (pw_receive != confirm_pwd_receive):
            return jsonify({'msg': '패스워드 재입력 확인 바랍니다.'})
        else:
            find_id = db.user_info.find_one({'ID': id_receive})

            if (find_id == None):
                doc = {
                    'ID': id_receive,
                    'PWD': pw_receive,
                    'EMAIL': email_receive
                }
                db.user_info.insert_one(doc)
                return jsonify({'msg': '회원가입 완료'})
            else:
                return jsonify({'msg': '아이디가 이미 존재합니다!'})
     """

    find_id = db.user_info.find_one({'ID': id_receive})

    if (find_id == None):
        doc = {
            'ID': id_receive,
            'PWD': pw_hash,
            'EMAIL': email_receive
        }
        db.user_info.insert_one(doc)
        return jsonify({'result': 'success', 'msg': '회원가입 완료'})
        # return jsonify({"result": "success"})
    else:
        return jsonify({"result": "fail", "msg": "아이디가 이미 존재합니다!"})
        # return jsonify({"result": "fail"})


# ------------------------------- 중복검사 api / lsm -------------------------------
## 중복검사
@app.route('/api/check', methods=['POST'])
def check():
    id_receive = request.form['id_give']

    find_id = db.user_info.find_one({'id': id_receive})

    if (find_id != None):
        return jsonify({'msg': '중복된 아이디입니다.'})
    else:
        return jsonify({'msg': '사용 가능한 아이디입니다.'})
#---------------------------------------------------------------------------------------------------------




# ---------------- 리스트 페이지 : 기능 ----------------------------------------------------------------------
# ---------------------------------------------------POST  //  cyj
@app.route('/memo', methods=['POST'])
def art():
    title_receive = request.form['title_give']
    date_receive = request.form['date_give']
    place_receive = request.form['place_give']
    attendance_receive = request.form['attendance_give']
    content_receive = request.form['content_give']
    if (title_receive == ''):
        return jsonify({'msg': '제목을 입력해주세요.'})
    elif (date_receive == ''):
        return jsonify({'msg': '날짜를 입력해주세요.'})
    elif (place_receive == ''):
        return jsonify({'msg': '장소를 입력해주세요.'})
    elif (attendance_receive == ''):
        return jsonify({'msg': '참석인원을 입력해주세요.'})
    elif (content_receive == ''):
        return jsonify({'msg': '설명을 입력해주세요.'})
    else:
        doc = {'title': title_receive,
               'date': date_receive,
               'place': place_receive,
               'attendance': attendance_receive,
               'content': content_receive}
        db.write_info.insert_one(doc)
        return jsonify({'msg': '작성완료!', 'result': 'success'})

# ---------------------------------------------------GET 진행중 //  cyj
"""
@app.route('/list')
def list():
    contents = list(db.write_info.find({}, {"_id": False}))
    return render_template("list.html", contents=contents)
"""
#---------------------------------------------------------------------------------------------------------
>>>>>>> 05fac375bbfc5789ef3cd006685ccd4c44e73ca2


# ---------------------------------------------------------------------------------------------------------


# ---------------- 회원가입 페이지 : 기능 ----------------------------------------------------------------------
# ------------------------------- 회원가입 api / lsm -------------------------------
## 회원가입
@app.route('/api/membership', methods=['POST'])
def membership():
    id_receive = request.form['id_give']
    pw_receive = request.form['pwd_give']
    email_receive = request.form['email_give']

    find_id = db.user_info.find_one({'ID': id_receive})

    if (find_id == None):
        doc = {
            'ID': id_receive,
            'PWD': pw_receive,
            'EMAIL': email_receive
        }
        db.user_info.insert_one(doc)
        return jsonify({'msg': '회원가입 완료'})
    else:
        return jsonify({'msg': '아이디가 이미 존재합니다!'})


# ------------------------------- 중복검사 api / lsm -------------------------------
## 중복검사
@app.route('/api/check', methods=['POST'])
def check():
    id_receive = request.form['id_give']

    find_id = db.user_info.find_one({'ID': id_receive})

    if (find_id == None):
        return jsonify({'msg': '중복된 아이디입니다.'})
    else:
        return jsonify({'msg': '사용 가능한 아이디입니다.'})


# ---------------------------------------------------------------------------------------------------------


# ---------------- 리스트 페이지 : 기능 ----------------------------------------------------------------------
# ---------------------------------------------------POST  //  cyj
@app.route('/memo', methods=['POST'])
def art():
    title_receive = request.form['title_give']
    date_receive = request.form['date_give']
    place_receive = request.form['place_give']
    attendance_receive = request.form['attendance_give']
    content_receive = request.form['content_give']
    doc = {'title': title_receive,
           'date': date_receive,
           'place': place_receive,
           'attendance': attendance_receive,
           'content': content_receive}
    db.write_info.insert_one(doc)
    return jsonify({'msg': '작성완료!'})


# ---------------------------------------------------GET 진행중 //  cyj
@app.route('/list')
def list():
    asd = list(db.asd.find({}, {"_id": False}))
    return render_template("list.html", asd=asd)


# ---------------------------------------------------------------------------------------------------------


"""
# ----------------mongodb test data 생성작업을 위한 코드-----------------------------------
@app.route('/join', methods=['POST'])
def saving():
    id_give = request.form['id_give']
    pwd_give = request.form['pwd_give']
    email_give = request.form['email_give']

    doc = {
        'ID':id_give,
        'PWD':pwd_give,
        'EMAIL':email_give,
    }

    db.user_info.insert_one(doc)

    return jsonify({'msg':'저장이 완료되었습니다!'})
"""

if __name__ == '__main__':
<<<<<<< HEAD
    app.run('0.0.0.0', port=5004, debug=True)
=======
   app.run('0.0.0.0',port=5003,debug=True)

>>>>>>> 05fac375bbfc5789ef3cd006685ccd4c44e73ca2
