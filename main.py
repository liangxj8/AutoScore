import re
import configparser
import pyjw
import wechat
from CASLogin import cas_logout


def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')
    # 获取新条目
    username = config['CAS']['NetID']
    password = config['CAS']['password']
    try:
        text = pyjw.get_score(username, password)
        new_record_count = re.findall("recordCount:.*,name", text)[0]
    except IndexError:
        cas_logout()
        text = pyjw.get_score(username, password)
        new_record_count = re.findall("recordCount:.*,name", text)[0]
    # 监视运行时获取到的响应内容
    with open('record.txt', 'w') as fobj:
        fobj.write(text + '\n\n')
    record_count = config['jwxt']['recordCount']
    new_record_count = new_record_count.lstrip('recordCount:').rstrip(',name')
    if record_count == new_record_count:
        print("No new score.")
    else:
        config['jwxt']['recordCount'] = new_record_count
        result = eval(re.findall(r'\[.*\]', text)[0])
        for resource in result:
            if not (resource['resource_id']) in config['jwxt']:
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
