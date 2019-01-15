"""
这个模块用于存放我们编写的命令
"""

import random

import requests

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


@on_command('知乎日报')
def _(bot, ctx, arg):
    STORY_URL_FORMAT = 'https://daily.zhihu.com/story/{}'

    resp = requests.get(
        'https://news-at.zhihu.com/api/4/news/latest',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
    )

    data = resp.json()
    stories = data.get('stories')

    if not stories:
        bot.send(ctx, '暂时没有数据，或者服务无法访问')
        return

    reply = ''
    for story in stories:
        url = STORY_URL_FORMAT.format(story['id'])
        title = story.get('title', '未知内容')
        reply += f'\n{title}\n{url}\n'

    bot.send(ctx, reply)
