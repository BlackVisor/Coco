import base64
from Crypto.Cipher import AES
import gzip


class AppOutEncrypt:

    def __init__(self):
        self.mode = AES.MODE_ECB
        self.appKey = "6mpQfK5BSzzOfrZ6"
        # content1是url中截取的raw data
        self.content1 = ''

    def encrypt(self):
        # AES拼接的padding长度为字节总数进行计算
        padLen = 16 - (len(self.content1.encode('utf-8')) % 16)
        self.content2 = self.content1
        # AES/ECB/PKCS5PADDING拼接的字符数量就是要拼接的字符
        for i in range(padLen):
            self.content2 = self.content2 + chr(padLen)
        cryptor = AES.new(self.appKey, self.mode)
        self.content2 = cryptor.encrypt(self.content2)
        return self.content2

    def compress(self):
        self.content3 = self.encrypt()
        self.content4 = gzip.compress(self.content3)
        return self.content4

    def encode(self):
        self.content5 = self.compress()
        # base64编码
        self.content6 = base64.b64encode(self.content5).decode('utf-8')
        print(self.content6)
        print('{"data":"'+self.content6+'","msg":"Success","status":"000"}')


# 六八3⃣️ 亦杰
encrypt = AppOutEncrypt()
encrypt.content1 = input('Input:')
encrypt.encode()
