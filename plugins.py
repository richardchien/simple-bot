"""
这个模块用于存放我们编写的命令
"""

import random

from command import on_command


@on_command('echo')
def echo(bot, ctx, arg):
    return {'reply': arg}


@on_command('喵一个')
def miao(bot, ctx, arg):
    return {'reply': '喵～'}


@on_command('随机数')
def _(bot, ctx, arg):
    return {'reply': str(random.randint(0, 100))}


@on_command('计算')
def _(bot, ctx, arg):
    expression = arg.strip()
    print(expression)
    return {'reply': str(eval(expression))}
