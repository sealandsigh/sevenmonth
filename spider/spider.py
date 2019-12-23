# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/23

import re
from urllib import request

#断点调试
class Spider():
    url = "http://theater.mtime.com/China_Beijing/"
    root_pattern = '<li class="clearfix">([\s\S]*?)</li>'
    title_pattern = 'title="([\s\S]*?)" target'
    # score_pattern = '<span class="([\s\S]*?)" mid'
    score_pattern = '<span class="score none" mid="\d">([\s\S]*?)</span>'
    real_score_pattern = '<span class="score" mid="\d">([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding="utf-8")
        return htmls

    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        datas = []
        title = re.findall(Spider.title_pattern, root_html[70])
        score = re.findall(Spider.score_pattern, root_html[70])
        real_score = re.findall(Spider.real_score_pattern, root_html[70])
        print(title,score,real_score)
        # for html in root_html:
        #     title = re.findall(Spider.title_pattern, html)
        #     score = re.findall(Spider.score_pattern, html)
        #     real_score = re.findall(Spider.real_score_pattern, html)
        #     if score == []:
        #         data = {'title':title,'score':real_score}
        #         datas.append(data)
        #     else:
        #         data = {'title': title, 'score': 0}
        #         datas.append(data)
        # print(datas)
        # return datas

    def __refine(self,datas):
        pass


    def go(self):
        htmls = self.__fetch_content()
        datas = self.__analysis(htmls)
        self.__refine(datas)

spider = Spider()
spider.go()
