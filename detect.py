#coding:utf-8
import os
import time
import sys
from time import strftime, localtime




PING_RESULT = 0
NETWORK_RESULT = 0

def ping():
  ''' ping 主备网络 '''
  result = os.system(u"ping -c 5 baidu.com")
  if result == 0:
      print("[检测结果]网络状态正常，请您继续网上冲浪~")
  else:
      print("[检测结果]网络未连接，正在尝试启动connection程序")
      run_conn()
  return result


#网络不通的时候尝试启动connection.py连接网络
def run_conn():
    os.system("python3 /login/connection.py")



if __name__ == '__main__':
#  while True:
  PING_RESULT = ping()
  print('[当前时间]'+ strftime("%Y-%m-%d %H:%M:%S", localtime()))
  print('******************网络状态检测完毕******************')
  print('\n\n\n\n\n')
  sys.exit()
#   if PING_RESULT == 0:
#        time.sleep(20)
#   else:
#    time.sleep(10)