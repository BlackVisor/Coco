import json
import xlwt


# api文档
with open("D:/Code/OfferPlus/APICheck/design.json", encoding='UTF-8') as fp:
    data1 = json.load(fp)
    # json_str=json.dumps(data)
    # print(data)
    # keys=data.keys()
    # print(keys)
    # print(type(keys))

# 实际返回
with open("D:/Code/OfferPlus/APICheck/real.json", encoding='UTF-8') as fp:
    data2 = json.load(fp)
    # data_login=data2["login"]


# 创建一个excel对象
book = xlwt.Workbook(encoding='utf-8')
# 添加一个sheet页
sheet = book.add_sheet('接口检查', cell_overwrite_ok=True)

m = 0
for key1 in data1.keys():

    i = 0
    sheet.write(i, m, key1)
    i = 1
    if isinstance(data1.get(key1), dict):
        for key_API in data1[key1].keys():
            # 行，列 ，值
            sheet.write(i, m, key_API)
            i = i + 1

l = 4
for key2 in data2.keys():

    k = 0
    # print(api_ACT, l)
    sheet.write(k, l, key2)
    k = 1
    if isinstance(data2[key2], dict):
        for key_ACT in data2[key2].keys():
            # 行，列，值
            sheet.write(k, l, key_ACT)
            k = k + 1

book.save('D:/Code/OfferPlus/APICheck/Contrast.xls')