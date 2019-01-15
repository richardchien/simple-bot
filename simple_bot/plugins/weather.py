from nonebot import on_command, CommandSession


@on_command('weather', aliases=['天气', '查天气'])
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查哪个城市呢？')
    date = session.get('date', prompt='你想查哪一天的？')
    await session.send('你查询的城市是' + city)
    await session.send('你想查询的日期是' + date)


@weather.args_parser
async def _(session: CommandSession):
    if session.is_first_run:
        return

    print(session.current_key)
    session.args[session.current_key] = session.current_arg_text
