from datetime import date
from logging import fatal
from urllib import request
import requests
from requests.api import post
from requests.cookies import cookiejar_from_dict
from urllib3.util.retry import Retry
import re
import sys
import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from time import strftime, localtime
from dingtalkchatbot.chatbot import DingtalkChatbot



def conn_success1():
    # WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=69d2bf17c6fb29f***************1b15df2488ff68be2ebf60037e4'
    secret = 'SECf062df5580fa058**********************62d31fc43704ec524805f695c06'  # 可选：创建机器人勾选“加签”选项时使用
    # 初始化机器人
    xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）

    # Text消息@所有人
    xiaoding.send_text(msg='网络连接成功！', is_at_all=False)


def conn_success2():
    message = MIMEText("网络连接成功！网上冲浪快乐！")  
    message['From'] = "{}".format("xxxxxx@qq.com")
    message['To'] = "*******@qq.com"
    message['Subject'] = "网络连接成功提醒" 
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  
        smtpObj.login("BitBot", "********************")  
        smtpObj.sendmail("xxxxxx@qq.com","*******@qq.com", message.as_string())  
        print("mail has been send successfully.(2)")
    except smtplib.SMTPException as e:
        print(e)


def conn_success3():
    message = MIMEText("网络连接成功！网上冲浪快乐！")  
    message['From'] = "{}".format("xxxxxx@qq.com")
    message['To'] = "********@qq.com"
    message['Subject'] = "网络连接成功提醒" 
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  
        smtpObj.login("BitBot", "********************")  
        smtpObj.sendmail("xxxxxx@qq.com","*********@qq.com", message.as_string())  
        print("mail has been send successfully.(3)")
    except smtplib.SMTPException as e:
        print(e)

def conn_success4():
    message = MIMEText("网络连接成功！网上冲浪快乐！")  
    message['From'] = "{}".format("xxxxxx@qq.com")
    message['To'] = "********@qq.com"
    message['Subject'] = "网络连接成功提醒" 
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  
        smtpObj.login("BitBot", "********************")  
        smtpObj.sendmail("xxxxxx@qq.com","*********@qq.com", message.as_string())  
        print("mail has been send successfully.(4)")
    except smtplib.SMTPException as e:
        print(e)



def GetInformation(url):
    """
    docstring
    """
    res=requests.get(url)
    str=res.text
    newurl=str[32:-12]
    return newurl

def GetCookie(url):
    """
    docstring
    """
    postdata=("userId="+"17600****")
    postdata+=("&password="+"00****")
    session=requests.Session()
    cookie_jar=session.post(url,postdata).cookies
    cookie=requests.utils.dict_from_cookiejar(cookie_jar)
    jsid=cookie['JSESSIONID']
    return jsid





if __name__ == "__main__": 
    
    newurl=GetInformation("http://123.123.123.123/")
    
    jsid=GetCookie(newurl)
    's=requests.session()'
    headers={
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN',
    'Cache-Control':'max-age=0',
    'Connection':'Keep-Alive',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
    'Host': '10.36.100.2:8181',
    'Referer':newurl,
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Program':'no-cache',
    'Content-Length': '404'
    }
    cookies={'EPORTAL_USER_GROUP':'2020%'+'E5%AD%A6%'+'E5%B9%B4','EPORTAL_AUTO_LAND':'','EPORTAL_COOKIE_OPERATORPWD':'',
    'EPORTAL_COOKIE_USERNAME':'',' EPORTAL_COOKIE_SERVER_NAME':'','EPORTAL_COOKIE_SERVER':'','EPORTAL_COOKIE_PASSWORD':'',
    'JSESSIONID':jsid}

    'http://10.36.100.2:8181/eportal/success.jsp?userIndex=33636335623335666430613365663136303261636130396562646330353035365f31302e38302e31342e36385f313736303032333135&keepaliveInterval=0'
    'http://10.36.100.2:8181/eportal/InterFace.do?method=login'

    '2020%E5%AD%A6%E5%B9%B4'

    # print(newurl)
    ip=re.findall(r'ip=(.*)&wlan',newurl)[0]
    name=re.findall(r'name=(.*)&ssid',newurl)[0]
    ssid=re.findall(r'ssid=(.*)&nasi',newurl)[0]
    nasip=re.findall(r'nasip=(.*)&mac',newurl)[0]
    mac=re.findall(r'mac=(.*)&t=',newurl)[0]
    url=re.findall(r'url=(.*)',newurl)[0]
    
    
    

    postdata=("userId=176002315&password=002315&service=&queryString="+"wlanuserip%253D"+ip+"%2526wlanacname%253D"+name+"%2526"+"ssid%253D"+ssid+"%2526nasip%253D"+nasip+"%2526mac%253D"+mac+"%2526t%253D"+"wireless-v2%2526"+"url%253D"+url+"&operatorPwd=""&operatorUserId=""&validcode=""&passwordEncrypt=false")
    
    rs=requests.post('http://10.36.100.2:8181/eportal/InterFace.do?method=login',headers=headers,cookies=cookies,data=postdata)
    rs.encoding='uft-8'
    print('[Version] 2020.11.26.15.52 ****************')
    print('[状态]开始连接网络Loading......')
    # print('自动连接返回信息:'+ rs.text)
    #将返回信息格式化为json便于判断网络连接结果
    try:
        responsetext = json.loads(rs.text)
        if responsetext['result'] == 'success':
            print('[运行结果]网络连接成功！')
            conn_success1()
            conn_success2()
            conn_success3()
            conn_success4()
        else:
            print('[运行结果]网络连接失败！')
            print('[失败原因]'+ responsetext['message'])
    except:
        print('[运行结果]未知错误，请查看日志！')
    sys.exit()

