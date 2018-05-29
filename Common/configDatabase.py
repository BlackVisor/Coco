import pymysql
from Common import readConfig
from Common.log import MyLog

localReadConfig = readConfig.ReadConfig()


class ConfigDatabase:
    global host, user, password, port, database, charset, config
    host = localReadConfig.getDatabase("host")
    user = localReadConfig.getDatabase("user")
    password = localReadConfig.getDatabase("password")
    port = localReadConfig.getDatabase("port")
    database = localReadConfig.getDatabase("database")
    charset = localReadConfig.getDatabase("charset")
    config = {
        'host': str(host),
        'port': int(port),
        'user': str(user),
        'password': str(password),
        'db': str(database),
        'charset': str(charset)
    }

    def __init__(self):
        # 日志输出
        # self.log = MyLog.getLog()
        # self.logger = self.log.logger
        self.db = None
        self.cursor = None

    def connectDatabase(self):
        try:
            # connect to db
            self.db = pymysql.connect(**config)

            # create cursor
            self.cursor = self.db.cursor()
            print("Connect to DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql):
        self.connectDatabase()
        # executing sql
        self.cursor.execute(sql)

        # executing by committing to db
        self.db.commit()
        return self.cursor

    def getAll(self, cursor):
        value = cursor.fetchall()
        return value

    def getOne(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDatabase(self):
        self.db.close()
        print("Database closed!")
