import json
from flask import Flask,request
import requests
import urllib3
import time

urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 3
s = requests.Session()
# 关闭多余连接
s.keep_alive = False
# 取消验证证书
s.verify = False
# 关闭在设置了verify=False后的错误提示
urllib3.disable_warnings()
app = Flask(__name__)

chatgpt_conversation=[]#AI对话形成上下文连贯

@app.route("/")
def hi():
    return "<p>hi!</p>"

@app.route("/webhook/event",methods=['POST'])
def event():#AI聊天
    global chatgpt_conversation
    proxies={'http':'http://127.0.0.1:7890','https':'https://127.0.0.1:7890'}#国内因为一些特殊原因无法访问chatgpt 所以需要FANQIANG，我使用的是Vpn链接：https://www.invitevp.com/#/register?code=7XniQ56k
    headers={'Content-Type': 'application/json','Authorization': 'Bearer 此处输入openai的apikey'}#Bearer加上空格然后替换openai的apikey 从openai官网获取
    json_data=json.loads(request.data)
    print(json_data)
    chatgpt_conversation.append({"role": "user", "content": json_data['text']['content']})
    json_message={
    "model": "gpt-3.5-turbo",
    "messages": chatgpt_conversation}
    chatgpt_response=requests.post('https://api.openai.com/v1/chat/completions',headers=headers,json=json_message,proxies=proxies)
    chatgpt_conversation.append(chatgpt_response.json()['choices'][0]['message'])
    answer=chatgpt_response.json()['choices'][0]['message']['content']
    print("----"*20)
    print(answer)
    print("----"*20)
    headers2={'Content-Type':'application/json'}
    json_sendmessages={"msgtype": "text","text": {"content":answer+'\r\n会话数:'+str(len(chatgpt_conversation))}}
    url='webhook地址从钉钉群聊机器人处获取'#样例：https://oapi.dingtalk.com/robot/send?access_token=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    response=requests.post(url,headers=headers2,json=json_sendmessages)
    print(response.text)
    if len(chatgpt_conversation)>16:#对会话数进行限制
        chatgpt_conversation=[]
    return '这只是一个回复'
@app.route("/webhook/images",methods=['POST'])
def images():#AI生产图片
    proxies={'http':'http://127.0.0.1:7890','https':'https://127.0.0.1:7890'}#国内因为一些特殊原因无法访问chatgpt 所以需要FANQIANG，我使用的是Vpn链接：https://www.invitevp.com/#/register?code=7XniQ56k
    headers={'Content-Type': 'application/json','Authorization': 'Bearer 此处输入openai的apikey'}#Bearer加上空格然后替换openai的apikey 从openai官网获取
    json_data=json.loads(request.data)
    print(json_data['text']['content'])
    json_message={
    "prompt": json_data['text']['content'],
    "n": 1,
    "size": "1024x1024"}
    chatgpt_response=requests.post('https://api.openai.com/v1/images/generations',headers=headers,json=json_message,proxies=proxies)
    json_data['text']['content']=chatgpt_response.json()['data'][0]['url']
    print("----"*20)
    print(chatgpt_response.json()['data'][0]['url'])
    print("----"*20)
    return json_data
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=18888,debug=True)#运行在有公网IP的服务器，同时开发18888端口