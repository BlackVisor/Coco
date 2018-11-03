from Decrypt import aesUtil

test1 = aesUtil.AppOutEncrypt()
test2 = aesUtil.AppOutDecrypt()
test3 = aesUtil.WebInEncrypt()
test4 = aesUtil.WebInDecrypt()
test5 = aesUtil.WebOutEncrypt()
test6 = aesUtil.WebOutDecrypt()


test = input('Input:')
test1.content1 = test
test2.content1 = test
test3.content1 = test
test4.content1 = test
test5.content1 = test
test6.content1 = test
# test1.appOutEncrypt()
# test2.appOutDecrypt()
# test3.webInEncrypt()
# test4.webInDecrypt()
# test5.webOutEncrypt()
test6.webOutDecrypt()