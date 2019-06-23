# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

my_friend = bot.friends().search('kira')[0]
allFriend = bot.friends() #所有好友

#my_friend = bot.chat()

# # 发送文本给好友
# my_friend.send('Hello gaorui hahhah!')
# # 发送图片

@bot.register() #注册接收信息
def recv_send_msg(msg):
    print('收到的信息:->',msg)
    if msg == '1':
        return '你要购买点卡嘛'
    else:
        print(msg)
        return '欢迎来到币酋社区'
    # 输出结果: hello
# 进入 Python 命令行、让程序保持运行
embed()
