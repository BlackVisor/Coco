# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : foos.py
# @Author: Cheng JiangDong
# @Date  : 2019/6/17
# @Desc  : Later equals never


class Father:
    name = "i am father"

    def myname(self):
        print(Father.name)


foo = Father()
foo.myname()