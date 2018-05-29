import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from Common.log import MyLog # 导入MyLog类
from Common import configHttp # 导入configHttp模块


global projectDirectory, resultPath
projectDirectory = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
localConfigHttp = configHttp.ConfigHttp()
log = MyLog.getLog()
logger = log.logger


# get testcase from excel
def getXls(xlsName, sheetName):
    cls = []

    # get xls file's path
    xlsPath = os.path.join(projectDirectory, "TestCase", xlsName)

    # open xls file
    file = open_workbook(xlsPath)

    # get sheet by name
    sheet = file.sheet_by_name(sheetName)

    # get one sheet's rows, nrows就是表的行数
    nrows = sheet.nrows
    for i in range(nrows):
        # sheet的第i行的第一列
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


# # get sql sentance from xml
# database = {}
#
#
# def setXml():
#     if len(database) == 0:
#         sqlpath = os.path.join(projectDirectory, "TestCase", "SQL.xml")
#         tree = ElementTree.parse(sqlpath)
#         for db in tree.findall("database"):
#             db_name = db.get("name")
#             # print(db_name)
#             table = {}
#             for tb in db.getchildren():
#                 table_name = tb.get("name")
#                 # print(table_name)
#                 sql = {}
#                 for data in tb.getchildren():
#                     sqlid = data.get("id")
#                     # print(sqlid)
#                     sql[sqlid] = data.text
#                 table[table_name] = sql
#             database[db_name] = table
#
#
# def get_xml_dict(database_name, table_name):
#     set_xml()
#     database_dict = database.get(database_name).get(table_name)
#     return database_dict
#
#
# def get_sql(database_name, table_name, sqlid):
#     db = get_xml_dict(database_name, table_name)
#     sql = db.get(sqlid)
#     return sql
