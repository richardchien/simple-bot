import os

import nonebot

from simple_bot import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        os.path.join(os.path.dirname(__file__), 'plugins'),
        'simple_bot.plugins')
    nonebot.run()
