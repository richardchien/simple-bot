from pprint import pprint
import random

from cqhttp import CQHttp

bot = CQHttp(api_root='http://127.0.0.1:5700')


# 私聊消息
@bot.on_message('private')
def handle_msg(ctx):  # 处理函数
    pprint(ctx)
    msg: str = ctx['message']
    if msg.startswith('echo '):
        return {'reply': msg[len('echo '):]}
    elif msg == '喵一个':
        return {'reply': '喵～'}
    elif msg == '随机数':
        bot.send(ctx, str(random.randint(0, 100)))
    elif msg.startswith('计算 '):
        expression = msg[len('计算 '):].strip()
        print(expression)
        bot.send(ctx, message=str(eval(expression)))


bot.run('127.0.0.1', 8080)
