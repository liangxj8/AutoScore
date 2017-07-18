# -*- coding: utf-8 -*-
import requests
import json
import configparser


# 获取access_token
def get_access_token(corpid, secret):
    payload = {'corpid': corpid, 'corpsecret': secret}
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    resp = requests.get(url, params=payload)
    access_token = eval(resp.text)['access_token']
    return access_token


# 发送文本消息
def message_send(userid, agentid, content, access_token):
    msg = {
        'touser': userid,
        'msgtype': 'text',
        'agentid': agentid,
        'text': {
            'content': content
        },
        'safe': 0
    }
    payload = {'access_token': access_token}
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send'
    resp = requests.post(url, params=payload, data=json.dumps(msg))
    return resp.text

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    CorpID = config['wechat']['CorpID']
    Secret = config['wechat']['Secret']
    ACCESS_TOKEN = get_access_token(CorpID, Secret)
    UserID = config['wechat']['UserID']
    AgentId = config['wechat']['AgentId']
    CONTENT = 'hello, world'
    print(message_send(UserID, AgentId, CONTENT, ACCESS_TOKEN))
