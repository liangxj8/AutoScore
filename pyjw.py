# -*- coding: utf-8 -*-
import re
import requests
from CASLogin import cas_login


def pyjw():
    url = 'https://cas.sysu.edu.cn/cas/login?service=http://uems.sysu.edu.cn/jwxt/casLogin?' \
          '_tocasurl=http://wjw.sysu.edu.cn/cas'
    resp = cas_login(url)
    url = re.findall(r'http://wjw.sysu.edu.cn/.*?&MU=', resp.text)[0]
    session = requests.Session()
    session.get(url)
    form = {'year': '2016-2017', 'term': '2', 'pylb': '01'}
    result = session.get('http://wjw.sysu.edu.cn/api/score', params=form, cookies=session.cookies).text
    print(re.findall(r'recordCount:[0-9]', result)[0])

if __name__ == '__main__':
    pyjw()
