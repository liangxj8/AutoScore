# -*- coding: utf-8 -*-
import re
import configparser
import pyjw
import wechat


def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')
    username = config['CAS']['NetID']
    password = config['CAS']['password']
    # 获取新条目
    text = pyjw.get_score(username, password)
    record_count = config['jwxt']['recordCount']
    new_record_count = re.findall("recordCount:.*,name", text)[0]
    new_record_count = new_record_count.lstrip('recordCount:').rstrip(',name')
    if record_count == new_record_count:
        print("No new score.")
    else:
        config['jwxt']['recordCount'] = new_record_count
        result = eval(re.findall(r'\[.*\]', text)[0])
        for resource in result:
            if not (resource['resource_id']) in config['jwxt']:
                # 组装请求，引用微信API推送文本消息
                corpid = config['wechat']['CorpID']
                secret = config['wechat']['Secret']
                access_token = wechat.get_access_token(corpid, secret)
                userid = config['wechat']['UserID']
                agentid = config['wechat']['AgentId']
                content = pyjw.show_score(result, resource['resource_id'])
                print(content, end='\n')
                print(wechat.message_send(userid, agentid, content, access_token), end='\n\n')
                config['jwxt'][resource['resource_id']] = 'resource_id'
        # 更新配置文件
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

if __name__ == '__main__':
    main()
