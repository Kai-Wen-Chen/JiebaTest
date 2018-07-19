# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:34:44 2018

@author: admin
"""
# this code reads and writes a text file in utf-8 format

import jieba
import os.path

textF = open(os.path.abspath("./jieba_test_utf8.txt"), "r")
text = textF.read()
text8 = text.decode('utf-8')

jieba.set_dictionary(os.path.abspath("./dict.txt.big"))
jieba.load_userdict('userdict.txt')
seg = jieba.cut(text, cut_all = False)

outputF = open("jieba_output.txt", "w")
strr = "/".join(seg)
outputF.write(strr.encode("utf-8"))

textF.close()
outputF.close()