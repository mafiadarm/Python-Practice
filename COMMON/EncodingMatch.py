#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_12_2018  11:05
    File Name:      /GitHub/EncodingMatch
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

import rsa
import base64
import hashlib
import logging
import binascii
# Crypto已经停用，安装Crypto的替代品
# linux pip install pycrytodome
# windows pip install pycrytodmex
from Cryptodome.Cipher import DES
from Cryptodome.Util import Counter
from Cryptodome import Random
from Cryptodome.Cipher import DES3
from Cryptodome.Cipher import AES
from urllib.parse import unquote, quote

__author__ = 'Loffew'


# logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def parse_quote(code):
    return "parse_quote", parse_quote(code)


def parse_unquote(code):
    i = parse_unquote(code)
    return "parse_unquote", i

def base64_encode_n(code):
    return "base64_encode_n", base64.encodebytes(code.encode())


def base64_encode_u(code):
    return "base64_encode_u", base64.b64encode(code.encode())


def base64_encode_d(code):
    return "base64_encode_d", base64.standard_b64encode(code.encode())


def base64_encode_s(code):
    return "base64_encode_s", base64.urlsafe_b64encode(code.encode())


def base64_decode(code):
    i = base64.b64decode(code)
    return "base64_decode", i


def base64_decode_n(code):
    i = base64.decodebytes(code).decode()
    return "base64_decode_n", i


def base64_decode_u(code):
    i = base64.decodebytes(code).decode()
    return " base64_decode_u", i


def base64_decode_d(code):
    i = base64.standard_b64decode(code).decode()
    return "base64_decode_d", i


def base64_decode_s(code):
    i = base64.urlsafe_b64decode(code).decode()
    return "base64_decode_s", i


def md5_make(code):
    return "md5_make", hashlib.md5(code.encode()).hexdigest()


def md5_know(code):
    print("md5_know, ", end='')
    if len(code) == 32:
        return "may be MD5"
    return "not be MD5"


def des_encode(code):
    key = '-8B key-'  # 长度为8 [2,4,8]

    while len(code) % 8 != 0:  # 确保需要加密的文本是8的倍数
        code += " "

    key = key.encode()
    msg = code.encode()

    # nonce = Random.new().read(int(DES.block_size / 2))
    # ctr = Counter.new(int(DES.block_size * 8 / 2), prefix=nonce)
    # cipher = DES.new(key, DES.MODE_CTR, counter=ctr)
    # msg = nonce + cipher.encrypt(msg)
    # msg = binascii.b2a_hex(msg)

    # return "DES_encode", msg.decode()

    # 替换注释部分
    des = DES.new(key, DES.MODE_ECB)  # 创建DES实例
    encrypto_msg = des.encrypt(msg)

    return "DES_encode， key=%s" % key, encrypto_msg, "解密为:", des.decrypt(encrypto_msg)  # 加密结果和解密结果


def three_des_encode(code):
    key = 'Sixteen byte key'
    key = key.encode()
    msg = code.encode()
    iv = Random.new().read(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_OFB, iv)
    msg = iv + cipher.encrypt(msg)
    msg = binascii.b2a_hex(msg)
    return "3DEs_encode", msg.decode()


def aes_encode(code):
    key = b'Sixteen byte key'  # 加密放的公钥 要求16字节长度 [24 32]

    while len(code) % 16 != 0:
        code += " "

    msg = code.encode()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)  # 实例化
    msg = iv + cipher.encrypt(msg)
    # AES加密得到的字符串不一定是ascii字符集，输出到终端或者保存的时候可能出问题，所以把加密后的字符串转化为16进制
    return "AES_encode", binascii.b2a_hex(msg)


def aes_decode(code):
    key = b'Sixteen byte key'  # 解密需要公钥
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)  # 实例化
    msg = cipher.decrypt(binascii.a2b_hex(code)).decode()
    return "AES_decode", msg.rstrip(" ")  # 去掉右边所有的空格[strip是首尾，lstrip是左边所有的]


def rsa_encode(code):
    pubkey = 'EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443'
    rsa_n = int(pubkey, 16)  # 把16进制的key转换成 数字
    rsa_e = int('10001', 16)  # js里面一般是 parseInt('10001', 16)
    s = code.encode()  # 要转的内容进行编码
    key = rsa.PublicKey(rsa_n, rsa_e)  # 创建公钥
    message = rsa.encrypt(s, key)  # 把需要加密的文本写入公钥进行加密
    message = binascii.b2a_hex(message)  # 将加密信息转换为16进制
    return "RSA_encode", message.decode()


def url_decode(code):
    """解%E5%8F%B2%E4%B8%8A"""
    return "url解码", unquote(code)


def gbk_decode(code):
    """解 b'\xc4\xe3\xba\xc3'"""
    return "gbk解码", code.decode("gbk")


def gb2312_decode(code):
    """解 b'\xc4\xe3\xba\xc3'"""
    return "gb2312解码", code.decode("gb2312")


def utf8_decode(code):
    """解 b'\xc4\xe3\xba\xc3'"""
    return "utf8解码", code.decode("utf-8")


def double_decode(code):
    """解 b'\xc4\xe3\xba\xc3'"""
    return "utf8解码", code.encode().decode()


def random_decode(code):
    """自己随机组合各种编码转转转"""
    pass


def code_encode(code):
    coen = f""""url编码", {quote(code)}
"bgk编码", {code.encode('gbk')}
"gb2312", {code.encode('gb2312')}
"utf8", {code.encode('utf-8')}"""
    return coen


def main(code):
    print("-" * 30, "以下为加密", "-" * 30)
    for i in encode_func_list:
        try:
            print(i(code))
        except RecursionError:
            pass
        except AttributeError:
            pass
        except TypeError:
            pass
        except ValueError:
            pass

    print("-" * 30, "以下为解密", "-" * 30)
    for i in decode_func_list:
        try:
            print(i(code))
        except TypeError:
            pass
        except RecursionError:
            pass
        except Exception:
            pass

    print("-" * 30, "以下为4种常见编码", "-" * 30)
    try:
        print(code_encode(code))
    except AttributeError:
        pass

    print("-" * 30, "以下为解编码", "-" * 30)
    for i in code_change_list:
        try:
            print(i(code))
        except TypeError:
            pass
        except RecursionError:
            pass
        except Exception:
            pass

    print("-" * 30, "以下为RSA解码和编码", "-" * 30)

    try:
        en = rsaEncrypt(ss)
        print(en)
        de = rsaDecrypt(en[1])
        print(de)
    except RecursionError:
        pass
    except AttributeError:
        pass
    except TypeError:
        pass



def rsaEncrypt(code):
    text = rsa.encrypt(code.encode(), public_key)
    return "rsaEncrypt", binascii.b2a_hex(text)


def rsaDecrypt(code):
    text = rsa.decrypt(binascii.a2b_hex(code), private_key)
    return "rsaDecrypt", text.decode()

if __name__ == '__main__':
    # 以下模拟RSA公钥加密哦，私钥解密过程
    public_key, private_key = rsa.newkeys(1024)

    encode_func_list = [parse_quote, base64_encode_n, base64_encode_u, base64_encode_d, base64_encode_s, md5_make,
                        des_encode, three_des_encode, aes_encode, rsa_encode]
    decode_func_list = [parse_unquote, base64_decode_n, base64_decode_u, base64_decode_d, base64_decode_s, md5_know, base64_decode, ]

    code_change_list = [url_decode, gbk_decode, gb2312_decode, utf8_decode, double_decode, random_decode, ]

    """
    unicode编码前面要加u，bytes编码前要加b
    u'\u559c\'
    b'%40%50%60'
    """
    ss = ""
    # print(base64_decode(ss))
    main(ss)
    print("-" * 60)






