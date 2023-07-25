#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     en_de_cryption2.py
# author:   zlw2008ok@126.com
# date:     2023/7/19
# desc:     用python实现对文件数据进行加密并保存新文件，同时实现对加密文件进行读取然后进行解密。
#
# cmd>e.g.:  
# *****************************************************
from cryptography.fernet import Fernet
import os


# 生成密钥并保存
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


# 从文件中加载密钥
def load_key():
    return open("secret.key", "rb").read()


# 使用给定的密钥对文件进行加密
def encrypt_file(filename, key):
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("encrypted_" + filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)


# 使用给定的密钥对文件进行解密
def decrypt_file(filename, key):
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open("decrypted_" + filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted)


# 创建密钥
generate_key()

# 加载密钥
key = load_key()

# 加密文件
encrypt_file("test.txt", key)

# 解密文件
decrypt_file("encrypted_test.txt", key)