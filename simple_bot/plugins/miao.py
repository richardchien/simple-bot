from nonebot import on_command, CommandSession


@on_command('miao', aliases=['喵一个', '喵喵喵', '喵'])
async def _(session: CommandSession):
    await session.send('喵～')
