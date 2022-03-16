from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://{user}:{pw}@{url}/{db}'.format(
    user='root',
    pw='root',
    url='db',
    db='lim2'

)  # 본인이 사용할 DB url를 설정해줌 mysql를 사용하고 mysql://{user}:{pw}@{url}/{db}/
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #sqlalchemy의 이벤트를 처리하는 옵션이다 하지만 사용하지 않아서 False를 해준다
CORS(app)

db = SQLAlchemy(app) #db는 SQLAlchemy 객체이다


class Shop():
    id = db.Column(db.Integer, primary_key=True, autoincrement=False) #autoincrement 는 True 를 해주면 1씩 증가 시켜준다 primarykey 를 자동으로 
    name = db.Column(db.String(200)) #빈 값 허용할 때는 nullable=True
    shop_address = db.Column(db.String(200))

class Order():
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop = db.Column(db.Integer)  
    address = db.Column(db.String(200))



@app.route('/')
def index():
    return 'hello'

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')