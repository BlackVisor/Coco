import pymysql
import configparser


class GetToken:

    def __init__(self):
        self.userId = 0
        self.serverType = ''

    config = configparser.ConfigParser()
    config.read('D:/Code/OfferPlus/config.ini')

    connect = pymysql.connect(host=config.get('database', 'dbHost'),
                              port=config.getint('database', 'dbPort'),
                              user=config.get('database', 'dbUser'),
                              passwd=config.get('database', 'dbPassword'),
                              db=config.get('database', 'dbTable'),
                              charset=config.get('database', 'dbCharSet'),
                              )

    cursor = connect.cursor()

    sql = 'select token_id from ejet_user_separate where user_id = %d and server_type = \'%s\'' % (config.getint('userInfo', 'userId'), config.get('userInfo', 'serverType'))
    cursor.execute(sql)
    tokenId = cursor.fetchone()

    cursor.close()
    connect.close()


a = GetToken()
print(a.tokenId)


