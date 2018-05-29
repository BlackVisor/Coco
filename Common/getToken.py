from Common.configDatabase import ConfigDatabase
import configparser


class GetToken:

    def __init__(self):
        self.userId = 0
        self.serverType = ''
        self.sql = ''

    connect = ConfigDatabase()

    config = configparser.ConfigParser()
    config.read('D:/Code/OfferPlus/Common/config.ini')

    sql = 'select token_id, app_type from ejet_user_separate where user_id = %d and server_type = \'%s\'' % (config.getint('user', 'userId'), config.get('user', 'serverType'))

    cursor = connect.executeSQL(sql)
    result = connect.getOne(cursor)
    token_id = result[0]
    # print(type(token_id))
    app_type = result[1]
    # print(type(app_type))
    connect.closeDatabase()
