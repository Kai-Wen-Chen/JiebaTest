# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:36:20 2018

@author: admin
"""
import jieba
import jieba.analyse
import os.path

Input = open(os.path.abspath('./jieba_test_utf8.txt'), 'rb')
Output = open(os.path.abspath('./extract_tags.txt'), 'w')

content = Input.read()

tags = jieba.analyse.extract_tags(content, 5)

for tag in tags:
    Output.write(tag.encode('utf-8') + ' ')

Input.close()
Output.close()