# 基于企业微信的中山大学成绩通知
## 一、第三方模块依赖
configparser, requests, bs4, re
## 二、config.ini配置文件说明
```ini
[CAS]
; 中山大学中央身份验证服务(CAS)
netid = ********
password = *****

[jwxt]
; 已出成绩的课程数
recordcount = 7
; 键名为已出成绩的课程的resource_id，方便查找
; 键值均为resource_id，不影响程序
15727965159 = resource_id
15825986105 = resource_id
15730612923 = resource_id
15900115586 = resource_id
15808149259 = resource_id
15825962046 = resource_id
15825958219 = resource_id

[wechat]
; 企业ID
corpid = ********
; 应用的凭证密钥
secret = ********
; 成员在企业微信通讯录中的ID
userid = ********
; 企业应用的id
agentid = *******
```