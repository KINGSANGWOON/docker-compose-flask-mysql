from main import app, db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager


migrate = Migrate(app,db) # migrate 해줄 대상을 적는다
manager = Manager(app)   # manage.py class 는 모든 명령어를 관리하고 command line 에서 어떻게 호출될지를 관리한다

manager.add_command('db',MigrateCommand) # migrate를 해줄 때 사용하는 command이다 

if __name__=='__main__':
    manager.run()



# python manager.py db init (python db를 초기화 해줄 때 사용한다)
# python manager.py db migrate (모델을 새로 생성하거나 변결할 때 사용)
# python manager.py db (모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용)