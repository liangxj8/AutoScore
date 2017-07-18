import re
import pyjw
import wechat

# 读取缓存
f = open('temp', 'r')
recordCount = f.read(13)
resource_id = f.readlines()
f.close()
# 获取新条目
text = pyjw.get_score()
if not recordCount == re.findall("recordCount:[0-9]", text)[0]:
    recordCount = re.findall("recordCount:[0-9]", text)[0]
    result = eval(re.findall(r'\[.*\]', text)[0])
    for resource in result:
        if not (resource['resource_id'] + '\n') in resource_id:
        	# secret
            CorpID = corpid
            Secret = corpsecret
            ACCESS_TOKEN = wechat.get_access_token(CorpID, Secret)
            UserID = "UserID1|UserID2|UserID3",
            AgentId = 1
            CONTENT = pyjw.show_score(result, resource['resource_id'])
            print(CONTENT)
            print(wechat.message_send(UserID, AgentId, CONTENT, ACCESS_TOKEN))
    # 更新缓存
    f = open('temp', 'w')
    f.write(recordCount + '\n')
    for resource in result:
        f.write(resource['resource_id'] + '\n')
