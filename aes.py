#!/usr/bin/python
# coding:utf-8
from Crypto.Cipher import AES
import base64
block_size = AES.block_size
padling = ["\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x10","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f",]
pad_it = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)
key = ('soss' * 4).encode('utf-8')


def encrypt_aes(sourceStr):
    sourceStr = sourceStr.encode('utf-8')
    generator = AES.new(key, AES.MODE_ECB)
    crypt = generator.encrypt(pad_it(sourceStr))
    crypted = base64.b64encode(crypt)
    return crypted
 
 
def decrypt_aes(cryptedStr):
    generator = AES.new(key, AES.MODE_ECB)
    cryptedStr = base64.b64decode(cryptedStr)
    recovery = generator.decrypt(cryptedStr)
    for PADDING in padling:
        if PADDING in recovery:
            decryptedStr = recovery.rstrip(PADDING)
    return decryptedStr
