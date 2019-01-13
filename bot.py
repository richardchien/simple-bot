from pprint import pprint
import random

from cqhttp import CQHttp

bot = CQHttp(api_root='http://127.0.0.1:5700')


# 私聊消息
@bot.on_message('private')
def handle_msg(ctx):  # 处理函数
    pprint(ctx)
    msg = ctx['message']
    if msg.startswith('echo '):
        bot.send(ctx, msg[len('echo '):])
    elif msg == '喵一个':
        bot.send(ctx, '喵～')
    elif msg == '随机数':
        bot.send(ctx, str(random.randint(0, 100)))

# bot.run('127.0.0.1', 8080)
