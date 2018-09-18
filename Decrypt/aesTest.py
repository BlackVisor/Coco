from Decrypt import aesUtil

test1 = aesUtil.AppOutDecrypt()
test2 = aesUtil.WebInEncrypt()
test3 = aesUtil.WebInDecrypt()
test4 = aesUtil.WebOutDecrypt()
test5 = aesUtil.WebInEncrypt()

test = input('Input:')
try:
    test1.content1 = test
    test1.decrypt()
    pass
except:
    try:
        test3.content1 = test
        test3.decrypt()
        pass
    except:
        try:
            test4.content1 = test
            test4.urlDecode()
            pass
        except:
            try:
                test2.content1 = test
                test2.encode()
                pass
            except:
                print('都不行啊!!!')