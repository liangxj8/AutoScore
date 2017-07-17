# -*- coding: utf-8 -*-
import requests
import json


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
	# secret
    CorpID = corpid
    Secret = corpsecret
    ACCESS_TOKEN = wechat.get_access_token(CorpID, Secret)
    UserID = "UserID1|UserID2|UserID3",
    AgentId = 1
    CONTENT = "hello, world"
    print(wechat.message_send(UserID, AgentId, CONTENT, ACCESS_TOKEN))
