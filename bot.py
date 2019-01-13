"""
这个模块用于接收 酷Q 消息，并调用对应命令的处理函数
"""

from pprint import pprint

from cqhttp import CQHttp

import tuling  # 导入图灵模块
import plugins  # 导入所有命令，虽然后面没有直接用到，但不能删掉
from command import command_handlers

bot = CQHttp(api_root='http://127.0.0.1:5700')


# 注册私聊消息处理函数
@bot.on_message('private')
def handle_msg(ctx):
    pprint(ctx)
    msg: str = ctx['message']
    sp = msg.split(maxsplit=1)
    if not sp:
        return

    cmd, *remained = sp
    arg = ''.join(remained)
    print('cmd:', cmd)
    print('arg:', arg)

    handler = command_handlers.get(cmd)
    print('handler:', handler)

    if handler:
        return handler(bot, ctx, arg)
    else:
        replies = tuling.get_reply(msg)
        if replies:
            return {'reply': replies[0]}


bot.run('127.0.0.1', 8080)
