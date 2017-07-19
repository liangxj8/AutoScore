# -*- coding: utf-8 -*-
import re
import requests
from CASLogin import cas_login

session = requests.Session()


def get_kclb(kclb):
    d = {'10': '公必', '11': '专必', '21': '专选', '30': '公选'}
    return d[kclb]


def get_score(username=None, password=None):
    url = 'https://cas.sysu.edu.cn/cas/login?service=http://uems.sysu.edu.cn/jwxt/casLogin?' \
          '_tocasurl=http://wjw.sysu.edu.cn/cas'
    resp = cas_login(url, username, password)

    url = re.findall(r'http://wjw.sysu.edu.cn/.*?&MU=', resp.text)[0]
    session.get(url)
    # 要获取成绩的学年及学期，pylb参数含义不明（拼不出来啊2333
    form = {'year': '2016-2017', 'term': '2', 'pylb': '01'}
    return session.get('http://wjw.sysu.edu.cn/api/score', params=form, cookies=session.cookies).text


def get_detail(resource_id):
    form = {'resource_id': resource_id}
    detail = session.get('http://wjw.sysu.edu.cn/api/score_detail', params=form, cookies=session.cookies).text
    result = eval(re.findall(r'\[.*\]', detail)[0])
    details = ""
    for ResultDict in result:
        details += ResultDict['cjpdlb'] + '：' + ResultDict['fxyscj'] + '\n'
    return details


def show_score(result=None, resource_id=None):
    if not result:
        result = eval(re.findall(r'\[.*\]', get_score())[0])
    if resource_id:
        for ResultDict in result:
            if resource_id == ResultDict['resource_id']:
                break
        msg = get_kclb(ResultDict['kclb']) + '：'
        msg += ResultDict['kcmc'] + '\n'
        msg += '绩点：' + ResultDict['jd'] + ' '
        msg += '教学班排名：' + ResultDict['jxbpm'].replace('\/', '/') + '\n'
        msg += '学分：' + ResultDict['xf'] + ' '
        msg += '最终成绩：' + ResultDict['zzcj'] + '\n'
        msg += get_detail(resource_id)
        return msg.rstrip('\n')
    else:
        msg = '类型 课程 学分 成绩 绩点 排名\n'
        for ResultDict in result:
            msg += get_kclb(ResultDict['kclb']) + ' '
            msg += ResultDict['kcmc'] + ' '
            msg += ResultDict['xf'] + ' '
            msg += ResultDict['zzcj'] + ' '
            msg += ResultDict['jd'] + ' '
            msg += ResultDict['jxbpm'].replace('\/', '/') + '\n'
        return msg

if __name__ == '__main__':
    print(show_score())
