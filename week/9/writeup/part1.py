#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashlist = open("../hashes", 'r')

words = wordlist.read().split()
hashes = hashlist.read().split()
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase


for hash in hashes:
    hash = hash.rstrip()
    for word in words:
        word = word.rstrip()
        for salt in salts:
            password = hashlib.sha512(salt + word).hexdigest()
            if (hash == password):
                print("Password: " + word + "\n" + "Salt: " + salt + "\n" +
                "Hash: " + hash + "\n")
