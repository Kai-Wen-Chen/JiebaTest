# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:41:51 2018

@author: admin
"""

import jieba
import jieba.analyse
import os.path

Input = open(os.path.abspath('./jieba_test_utf8.txt'), 'rb')
Output = open(os.path.abspath('./keywords_with_stop_words.txt'), 'w')

content = Input.read()

#jieba.analyse.set_stop_words("./stop_words.txt")
jieba.analyse.set_stop_words("./stop_words2.txt")
jieba.analyse.set_idf_path("./idf.txt.big");

tags = jieba.analyse.extract_tags(content, 5)

for tag in tags:
    Output.write(tag.encode('utf-8') + ' ')

Input.close()
Output.close()