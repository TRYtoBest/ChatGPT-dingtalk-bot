# ChatGPT-接入钉钉群聊机器人
ChatGPT接入钉钉群聊机器人
python 版本 3.9 作者未测试其他版本
会话数限制在18


__准备：钉钉群，一台有公网IP的服务器（把webhook.py脚本部署在这台服务器上），chatgpt账号并且获取apikey__

## 第一步：在钉钉开放平台https://open.dingtalk.com/   设置

进入我的后台->应用开发—>企业内部开发->机器人->创建应用 使用旧版

![image](https://user-images.githubusercontent.com/13046955/227491759-5224a868-bb68-4124-96cd-eedec1dc7bb8.png)
在开发管理设置白名单IP 和消息接收地址： http://IP:18888/webhook/event   （机器人被@以后会转发至该服务器）
![image](https://user-images.githubusercontent.com/13046955/227498806-daad27b8-f5a0-490e-ad75-158b27ac7f89.png)
在权限管理把权限都申请
![image](https://user-images.githubusercontent.com/13046955/227494155-9d62ca37-7ab7-4db1-b7aa-e1cf1355da81.png)
点击版本管理与发布的调试 可加入测试群聊
![image](https://user-images.githubusercontent.com/13046955/227494509-f1103b79-c59b-4d4b-a712-d2ca942a7efa.png)

添加

## 第二步：需要的模块
```
pip install -r requirements.txt
```
## 第三步： 在钉钉群群聊添加机器人并获取机器人的webhook地址

![image](https://user-images.githubusercontent.com/13046955/227495146-0bbf6682-fe15-435a-8a89-3159ba8cadd3.png)

如下图配置

![image](https://user-images.githubusercontent.com/13046955/227495862-e5fbacfe-13c5-4710-9ab2-4a032991ddcb.png)

然后修改代码把webhook地址和chatgpt的apikey替换上

![image](https://user-images.githubusercontent.com/13046955/227497525-aeab8179-8ffc-4e06-8b55-1c0b213b76d3.png)

测试效果如下:
![image](https://user-images.githubusercontent.com/13046955/227504385-206d04fe-216b-4b60-b7c0-520afd49ddce.png)


群聊效果如下：

![image](https://user-images.githubusercontent.com/13046955/227504468-5cc306cc-7e78-47b3-a11b-6bb7d4278305.png)


![image](https://user-images.githubusercontent.com/13046955/227497925-d81357c5-5a03-4e0d-a554-4ac8aab57b1e.png)


生成AI图片效果如下：（创建新的机器人，其他同上，消息接收地址设置
http://IP:18888/webhook/images）
![image](https://user-images.githubusercontent.com/13046955/227505080-47e2df90-c3bb-449e-9011-75e256c636a1.png)

有问题记得反馈！



