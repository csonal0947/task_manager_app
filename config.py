import os
class config:
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:root@localhost/Task_db'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SECRET_KEY=os.urandom(24)

