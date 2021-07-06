import pyDes, binascii


class DES():
    # 初始化key
    def __init__(self, key):
        self.key = key

    def des_encrypt(self, s):
        secret_key = self.key
        k = pyDes.des(secret_key, pyDes.triple_des, pad=None, padmode=pyDes.PAD_PKCS5)
        en = k.encrypt(s.encode("utf8"), padmode=pyDes.PAD_PKCS5)
        return binascii.b2a_hex(en)

    def des_descrypt(self, s):
        secret_key = self.key
        k = pyDes.des(secret_key, pyDes.triple_des, pad=None, padmode=pyDes.PAD_PKCS5)
        de = k.decrypt(binascii.a2b_hex(s), padmode=pyDes.PAD_PKCS5)
        return de

if __name__ == "__main__":
    # 秘钥最长8位，超过8位的舍弃
 test = DES("CueaiPrW")
 print(test.des_encrypt("1234"))