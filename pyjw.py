# -*- coding: utf-8 -*-
import re

import requests

from CASLogin import cas_login


def get_kclb(kclb):
    d = {'10': '公必', '11': '专必', '21': '专选', '30': '公选'}
    return d[kclb]


def get_score():
    url = 'https://cas.sysu.edu.cn/cas/login?service=http://uems.sysu.edu.cn/jwxt/casLogin?' \
          '_tocasurl=http://wjw.sysu.edu.cn/cas'
    resp = cas_login(url)

    url = re.findall(r'http://wjw.sysu.edu.cn/.*?&MU=', resp.text)[0]
    session = requests.Session()
    session.get(url)
    form = {'year': '2016-2017', 'term': '2', 'pylb': '01'}
    return session.get('http://wjw.sysu.edu.cn/api/score', params=form, cookies=session.cookies).text


def show_score():
    result = eval(re.findall(r'\[.*\]', get_score())[0])
    print('类型 课程 教师 学分 成绩 绩点 排名')
    for ResultDict in result:
        print(get_kclb(ResultDict['kclb']), end=' ')
        print(ResultDict['kcmc'], end=' ')
        print(ResultDict['jsxm'], end=' ')
        print(ResultDict['xf'], end=' ')
        print(ResultDict['zzcj'], end=' ')
        print(ResultDict['jd'], end=' ')
        print(ResultDict['jxbpm'].replace('\/', '/'), end='\n')

if __name__ == '__main__':
    show_score()
