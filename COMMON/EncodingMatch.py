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
from Crypto.Cipher import DES
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Cipher import DES3
from Crypto.Cipher import AES


__author__ = 'Loffew'

# logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def parse_quote(code):
    return parse_quote(code)

def parse_unquote(code):
    try:
        i = parse_unquote(code)
        return i
    except TypeError:
        pass
    except RecursionError:
        pass

def base64_encode_n(code):
    return "这是base64：",base64.encodebytes(code.encode())

def base64_encode_u(code):
    return base64.b64encode(code.encode())

def base64_encode_d(code):
    return base64.standard_b64encode(code.encode())

def base64_encode_s(code):
    return base64.urlsafe_b64encode(code.encode())

def base64_decode_n(code):
    i = base64.decodebytes(code).decode()
    return i

def base64_decode_u(code):
    i = base64.decodebytes(code).decode()
    return i

def base64_decode_d(code):
    i = base64.standard_b64decode(code).decode()
    return i

def base64_decode_s(code):
    i = base64.urlsafe_b64decode(code).decode()
    return i


def md5_make(code):
    return hashlib.md5(code.encode()).hexdigest()

def md5_know(code):
    if len(code) == 32:
        return "may be MD5"
    return

def des_encode(code):
    key = '-8B key-'  # 长度为8 [2,4,8]
    key = key.encode()
    msg = code.encode()
    nonce = Random.new().read(int(DES.block_size / 2))
    ctr = Counter.new(int(DES.block_size * 8 / 2), prefix=nonce)
    cipher = DES.new(key, DES.MODE_CTR, counter=ctr)
    msg = nonce + cipher.encrypt(msg)
    msg = binascii.b2a_hex(msg)
    return msg.decode()

def three_des_encode(code):
    key = 'Sixteen byte key'
    key = key.encode()
    msg = code.encode()
    iv = Random.new().read(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_OFB, iv)
    msg = iv + cipher.encrypt(msg)
    msg = binascii.b2a_hex(msg)
    return msg.decode()

def aes_encode(code):
    key = b'Sixteen byte key'  # 加密放的公钥
    msg = code.encode()
    iv = Random.new().read(AES.block_size)  # 16字节长度
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(msg)
    return binascii.b2a_hex(msg)

def aes_decode(code):
    key = b'Sixteen byte key'  # 解密需要公钥
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg1 = cipher.decrypt(code)
    return msg1[16:]

def rsa_encode(code):
    pubkey = 'EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443'
    rsa_n = int(pubkey, 16)
    rsa_e = int('10001', 16)  # js里面一般是 parseInt('10001', 16)
    s = code.encode()
    key = rsa.PublicKey(rsa_n, rsa_e)  # 创建公钥
    message = rsa.encrypt(s, key)  # 加密
    message = binascii.b2a_hex(message)  # 将加密信息转换为16进制
    return message.decode()


def main(code):
    for i in encode_func_list:
        try:
            print(i, i(code))
        except RecursionError:
            pass

    for i in decode_func_list:
        try:
            print(i, i(code))
        except TypeError:
            pass
        except RecursionError:
            pass
        except Exception:
            pass


if __name__ == '__main__':
    encode_func_list = [parse_quote, base64_encode_n, base64_encode_u, base64_encode_d, base64_encode_s, md5_make, des_encode, three_des_encode, aes_encode, rsa_encode]
    decode_func_list = [parse_unquote, base64_decode_n, base64_decode_u, base64_decode_d, base64_decode_s, md5_know, aes_decode]
    ss = 'abcdefg'
    main(ss)
