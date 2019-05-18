# Packages
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Std Packages
import time
import random
import os
import os.path as path

# Modules
import msg
import race

description = '''ゼルダ日本サーバー向けのレース補助Botです。
'''
bot = commands.Bot(command_prefix='!', description=description)
races = {}

def make_seed():
    return str(random.randint(10000, 999999))

# 起動時に通知してくれる処理
@bot.event
async def on_ready():
    print(msg.MSG_RUN_THIS_BOT)

# コマンド処理

# レース開始コマンド
@bot.command()
async def start(ctx):
    if ctx.channel.id not in races:
        await ctx.send(msg.MSG_RACE_CREATE)
        races[ctx.channel.id] = race.Race(ctx.channel.id)
    else:
        await ctx.send(msg.MSG_CONF_EXIST)

@bot.command()
async def restart(ctx):
    if ctx.channel.id in races:
        await ctx.send(msg.MSG_RE_START)
    else:
        await ctx.send(msg.MSG_RACE_CREATE)
    races[ctx.channel.id] = race.Race(ctx.channel.id)

# レース全般コマンド
@bot.command()
async def join(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        if ctx.author not in _race.entrant:
            # Userを追加
            _race.join(ctx.author)
            await ctx.send(str(ctx.author) + msg.MSG_USER_JOIN)
        else:
            await ctx.send(str(ctx.author) + msg.MSG_CONF_JOINED)
    else:
        await ctx.send(msg.MSG_NOT_START_RACE)

@bot.command()
async def count(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        if race.Race.RaceStat.READY == _race.status:
            # 走者がいない場合は警告して終了
            if len(_race.entrant) == 0:
                await ctx.send(msg.MSG_NO_ENTRANT)
            else:
                # カウントダウン
                msg_list = [msg.MSG_COUNT_DOWN_GO]
                if _race.bingoflag_oot:
                    msg_list.append(msg.URL_OOT_BINGO + make_seed())
                if _race.bingoflag_mm:
                    msg_list.append(msg.URL_MM_BINGO + make_seed())
                await ctx.send(msg.MSG_COUNT_DOWN_PREPARE)
                time.sleep(5)
                for i in range(5,0,-1):
                    await ctx.send(i)
                    time.sleep(1)
                for msg in msg_list:
                    await ctx.send(msg)
                    _race.start()
        else:
            await ctx.send(msg.MSG_NOT_START_RACE)

@bot.command()
async def entrant(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        entrant_str = msg.MSG_ENTRANT + '\n'
        for user in _race.entrant:
            entrant_str += '- ' + str(user) + '\n'
        await ctx.send(entrant_str)

@bot.command()
async def done(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        if race.Race.RaceStat.PROGRESS == _race.status:
            if ctx.author in _race.entrant:
                rank, time = _race.done(ctx.author)
                await ctx.send(str(rank) + '位：' + str(ctx.author) + ' - ' + time)

@bot.command()
async def result(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        result_str = ''
        for idx, result in enumerate(_race.results):
            result_str += '[' + str(idx + 1) + '] ' + result[0] + ' - ' + result[1] + '\n'
        await ctx.send(result_str)

@bot.command()
async def over(ctx):
    if ctx.channel.id in races:
        del races[ctx.channel.id]
        await ctx.send(msg.MSG_RACE_OVER)


@bot.command()
async def isrunning(ctx):
    await ctx.send(msg.MSG_BOT_IS_RUNNING)

@bot.command()
async def ootbingo(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        _race.bingoflag_oot = True
        await ctx.send(msg.MSG_SET_OOT_BINGO)
    
@bot.command()
async def mmbingo(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        _race.bingoflag_mm = True
        await ctx.send(msg.MSG_SET_MM_BINGO)

@bot.command()
async def unset_bingo(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        _race.bingoflag_oot = False
        _race.bingoflag_mm = False
        await ctx.send(msg.MSG_UNSET_BINGO)

@bot.command()
async def seed(ctx):
    await ctx.send(msg.MSG_MAKE_SEED_EXPL + make_seed())

@bot.command()
async def status(ctx):
    if ctx.channel.id in races:
        _race = races[ctx.channel.id]
        msg_list = [msg.MSG_STATUS]
        msg_list.append('時オカビンゴ：' + str(_race.bingoflag_oot))
        msg_list.append('ムジュラビンゴ：' + str(_race.bingoflag_mm))
        await ctx.send('\n'.join(msg_list))

@bot.command()
async def racebot(ctx):
    await ctx.send(msg.MSG_HELP)

# .envからアクセストークン取得
dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
discord_token = os.environ.get('DISCORD_BOT_TOKEN')

# botの接続と起動
# （botアカウントのアクセストークンを入れてください）
bot.run(discord_token)
