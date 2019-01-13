"""
这个模块用于提供注册命令的装饰器，和保存注册了的命令处理函数
"""

command_handlers = {}  # 键是命令名字，值是命令处理函数


def on_command(name):
    """
    用于将函数注册为命令

    :param name: 命令名
    """

    def decorator(func):
        command_handlers[name] = func
        return func

    return decorator
