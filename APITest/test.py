from Common import configDatabase
a = input('a:')
b = input('b:')
c = 299+0.5*12*int(a)+16.99*12*int(b)
if c < 1000:
    pass
elif c >= 1000 and c < 2000:
    c = 0.9*c
elif c <= 3000:
    c = 0.8*c
else:
    c = 0.7*c
print(c)

connect = configDatabase.ConfigDatabase()
sql = 'show columns from ejet_user_rela_company'
cursor = connect.executeSQL(sql)
result = connect.getAll(cursor)
connect.closeDatabase()
a = ''
for i in range(len(result)):
    a = a+result[i][0]+','

print(a)