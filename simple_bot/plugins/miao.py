from nonebot import on_command, CommandSession, on_request, RequestSession
from nonebot import permission as perm
from nonebot import CQHttpError


@on_command('miao', aliases=['喵一个', '喵喵喵', '喵'])
async def _(session: CommandSession):
    await session.send('喵～')


@on_command('get_member_count', aliases=['总人数'], permission=perm.GROUP,
            only_to_me=False)
async def _(session: CommandSession):
    try:
        member_list = await session.bot.get_group_member_list(
            group_id=session.ctx['group_id']
        )
    except CQHttpError:
        await session.send('无法获取')
        return

    await session.send(f'群里一共有 {len(member_list)} 个人')


@on_request('friend')
async def _(session: RequestSession):
    await session.approve()
