import base64
from Crypto.Cipher import AES
import io
import gzip
import re
import json
import urllib.parse
# pip install --use-wheel --no-index --find-links=https://github.com/sfbahr/PyCrypto-Wheels/raw/master/pycrypto-2.6.1-cp35-none-win_amd64.whl pycrypto  


class AppOutEncrypt:

    def __init__(self):
        self.mode = AES.MODE_ECB
        self.appKey = "6mpQfK5BSzzOfrZ6"
        # content1是url中截取的raw data
        self.content1 = ''

    def appOutEncrypt(self):

        # AES拼接的padding长度为字节总数进行计算
        padLen = 16 - (len(self.content1.encode('utf-8')) % 16)
        self.content2 = self.content1

        # AES/ECB/PKCS5PADDING拼接的字符数量就是要拼接的字符
        for i in range(padLen):
            self.content2 = self.content2 + chr(padLen)
        cryptor = AES.new(self.appKey, self.mode)
        self.content2 = cryptor.encrypt(self.content2)

        self.content4 = gzip.compress(self.content2)
        # base64编码
        self.content5 = base64.b64encode(self.content4).decode('utf-8')
        return '{"data":"' + self.content5 + '","msg":"Success","status":"000"}'

# input:'',output:'H4sIANad3VsC//vtL7X/yuKrqrH3l+eoVpt9BwDyLOt3EAAAAA=='


class AppOutDecrypt:

    def __init__(self):
        self.mode = AES.MODE_ECB
        self.appKey = "6mpQfK5BSzzOfrZ6"
        self.webKey = "viFZiOhDArcQTjkC"
        # content1是url中截取的raw data
        self.content1 = ''

    def appOutDecrypt(self):
        if re.match(r'(data=)+', self.content1):
            self.content2 = self.content1[5:]
        else:
            self.content2 = self.content1

        # 对content2进行base64解码
        self.content3 = base64.urlsafe_b64decode(self.content2)
        # 将解码得到的bytes解压
        buffer = io.BytesIO(self.content3)
        f = gzip.GzipFile(fileobj=buffer)
        self.content4 = f.read()

    # 将解压得到的bytes解密
        cryptor = AES.new(self.appKey, self.mode)
        self.content5 = cryptor.decrypt(self.content4).decode('utf-8')

        # 获取字符串最后一位的ascii表示，为string
        self.content6 = ord(self.content5[-1])

        # PKCS5Padding是缺几个字节就补充几个字节的几，好比缺6个字节，就补充6个字节的6，所以知道了填的是几，就能反推有几个几
        self.content7 = self.content5[0:-self.content6]
        return json.dumps(json.loads(self.content7), sort_keys=True, ensure_ascii=False, indent=4)

# input:'H4sIANad3VsC//vtL7X/yuKrqrH3l+eoVpt9BwDyLOt3EAAAAA==',output:''


class WebInEncrypt:

    def __init__(self):
        self.mode = AES.MODE_ECB
        self.appKey = "6mpQfK5BSzzOfrZ6"
        self.webKey = "viFZiOhDArcQTjkC"
        # content1是url中截取的raw data
        self.content1 = ''

    def webInEncrypt(self):
        padLen = 16 - len(self.content1.encode('utf-8')) % 16
        self.content2 = self.content1
        # AES/ECB/PKCS5PADDING拼接的字符数量就是要拼接的字符
        for i in range(padLen):
            self.content2 = self.content2 + chr(padLen)
        cryptor = AES.new(self.webKey, self.mode)
        self.content2 = cryptor.encrypt(self.content2)
        # base64编码
        self.content3 = base64.b64encode(self.content2).decode('utf-8')
        # urlencode编码为百分数形式
        self.content4 = urllib.parse.quote_plus(self.content3)
        return self.content4


# Test = AesUtils()
# # {"page":1,"pageNum":50}
# # raw：C7%2B0lxxEye%2FLnI8ABXJV3hTwbiZHRVx%2FEBSXNemtHDQ%3D
# # web：C7+0lxxEye/LnI8ABXJV3hTwbiZHRVx/EBSXNemtHDQ=
# Test.conten1 = input('待加密：')
# Test.encode()


class WebInDecrypt:

    def __init__(self):
        self.mode = AES.MODE_ECB
        self.appKey = "6mpQfK5BSzzOfrZ6"
        self.webKey = "viFZiOhDArcQTjkC"
        # content1是url中截取的raw data
        self.content1 = ''

    def webInDecrypt(self):
        if re.match(r'(data=)+', self.content1):
            self.content2 = self.content1[5:-24]
            # raw data copy过来是带百分号的
            self.content3 = urllib.parse.unquote(self.content2)
            self.content3 = base64.b64decode(self.content3)
        else:
            self.content2 = self.content1
            self.content3 = base64.b64decode(self.content2)
        cryptor = AES.new(self.webKey, self.mode)
        self.content4 = cryptor.decrypt(self.content3).decode('utf-8')

        # 获取字符串最后一位的ascii表示，为string
        self.content5 = ord(self.content4[-1])

        # PKCS5Padding是缺几个字节就补充几个字节的几，好比缺6个字节，就补充6个字节的6，所以知道了填的是几，就能反推有几个几
        self.content6 = self.content4[0:-self.content5]
        return json.dumps(json.loads(self.content6), sort_keys=True, ensure_ascii=False, indent=4)

# Test = WebInDecrypt()
# # data=KxCFJlTixPkqS6idIrLGofubSHKQwTadEeg%2FNl0uJGzjxj%2FggZZ9DY5LVfyQXQcoQ%2BfvEKaWhpnFSXsKyLtZUXKtLK82YzIFLB7m2l%2FPKuI%3D&timestamp=1517984853064
# # {"loginName":"1001200","password":"f492a324fbf16d306ee09f5d0ac5e1eb"}
# Test.content1 = input('待解密：')
# Test.decrypt()


class WebOutEncrypt:

    def __init__(self):
        self.mode = AES.MODE_ECB
        self.appKey = "6mpQfK5BSzzOfrZ6"
        self.webKey = "viFZiOhDArcQTjkC"
        # content1是要加密的json
        self.content1 = ''

    def webOutEncrypt(self):
        self.content2 = urllib.parse.quote(self.content1).encode('utf-8')
        self.content3 = gzip.compress(self.content2)
        self.content4 = base64.urlsafe_b64encode(self.content3)

        padLen = 16 - len(self.content4) % 16
        self.content5 = self.content4.decode('utf-8')
        # AES/ECB/PKCS5PADDING拼接的字符数量就是要拼接的字符
        for i in range(padLen):
            self.content5 = self.content5 + chr(padLen)
        cryptor = AES.new(self.webKey, self.mode)
        self.content6 = cryptor.encrypt(self.content5)

        self.content7 = base64.b64encode(self.content6)
        self.content8 = self.content7.decode('utf-8')
        return self.content8


class WebOutDecrypt:

    def __init__(self):
        self.mode = AES.MODE_ECB
        self.appKey = "6mpQfK5BSzzOfrZ6"
        self.webKey = "viFZiOhDArcQTjkC"
        # content1是url中截取的raw data
        self.content1 = ''

    def webOutDecrypt(self):
        if re.match(r'(data=)+', self.content1):
            self.content2 = self.content1[5:]
        else:
            self.content2 = self.content1

        # 对content2进行base64解码
        self.content3 = base64.urlsafe_b64decode(self.content2)
        # 将解码得到的bytes解密
        cryptor = AES.new(self.webKey, self.mode)
        self.content4 = cryptor.decrypt(self.content3).decode('utf-8')
        # 获取字符串最后一位的ascii表示，为string
        self.content5 = ord(self.content4[-1])
        # PKCS5Padding是缺几个字节就补充几个字节的几，好比缺6个字节，就补充6个字节的6，所以知道了填的是几，就能反推有几个几
        self.content6 = self.content4[0:-self.content5]
        self.content9 = base64.urlsafe_b64decode(self.content6)
        # 将解码得到的bytes解压
        buffer = io.BytesIO(self.content9)
        f = gzip.GzipFile(fileobj=buffer)
        self.content10 = f.read()
        #解压后的bytes解码为utf-8后再url解码
        self.content11 = urllib.parse.unquote(self.content10.decode('utf-8'))
        return json.dumps(json.loads(self.content11), sort_keys=True, ensure_ascii=False, indent=4)


# Test = WebOutDecrypt()
# # data=gV/mTZbaNpNczBowIekS3PPRt/lTGOP8OjlZyLO15p8n3CqULTC7Pq5+n/cs0ZA+vtPCkkErQTkYsZCGVV0Ui2TEk87eCrpjFlBLyJZ7x3Izp/4TpavvgYaoqnknZbBeGu9XOBjESCLXwgofqfG5uA==
# # {"contactNum":21,"receOfferNum":241,"myOfferNum":156,"sendOfferNum":86}
# Test.content1 = input('待解密：')
# Test.urlDecode()