#config.py
# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'



SECRET_KEY = "asdfasdfjasdfjasd;lf"

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'Azheng.*123'
DATABASE = 'database_learn'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "125795327@qq.com"
MAIL_PASSWORD = "ycillpfddoaybjia"
MAIL_DEFAULT_SENDER = "125795327@qq.com"