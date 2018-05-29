import json
import xlwt


# api文档
with open("D:/Code/Utils/APICheck/design.json", encoding='UTF-8') as fp:
    data1 = json.load(fp)
    # json_str=json.dumps(data)
    # print(data)
    # keys=data.keys()
    # print(keys)
    # print(type(keys))

# 实际返回
with open("D:/Code/Utils/APICheck/real.json", encoding='UTF-8') as fp:
    data2 = json.load(fp)
    # data_login=data2["login"]


# 创建一个excel对象
book = xlwt.Workbook(encoding='utf-8')
# 添加一个sheet页
sheet = book.add_sheet('接口检查', cell_overwrite_ok=True)

m = 0
for key1 in data1.keys():

    i = 0
    sheet.write(i, m, key1+"API文档")
    i = 1
    for key_API in data1['data'].keys():
        # 行，列 ，值
        sheet.write(i, m, key_API)
        i = i+1
    m = m+4


l = 2
for key2 in data2.keys():

    k = 0
    # print(api_ACT, l)
    sheet.write(k, l, key2 + "实际返回")
    k = 1
    for key_ACT in data2['data'].keys():
        # 行，列，值
        sheet.write(k, l, key_ACT)
        k = k+1
    l = l+4

book.save('D:/Code/Utils/APICheck/Contrast.xlsx')