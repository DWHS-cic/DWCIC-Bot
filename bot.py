import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()
TOKEN = os.getenv('TOKEN')

# 檢查 Token 是否存在
if not TOKEN:
    raise ValueError("錯誤：沒有找到 Discord Token！請確認 .env 檔案中已設定 TOKEN")

# 明確設定所需的意圖
intents = discord.Intents.default()
intents.members = True  # 啟用成員相關意圖
intents.guilds = True   # 啟用伺服器相關意圖

bot = commands.Bot(command_prefix='!', intents=intents)

async def update_roles():
    for guild in bot.guilds:
        roles = {
            '高三': discord.utils.get(guild.roles, name='高三'),
            '高二': discord.utils.get(guild.roles, name='高二'),
            '高一': discord.utils.get(guild.roles, name='高一'),
            '已畢業': discord.utils.get(guild.roles, name='已畢業')
        }
        
        async for member in guild.fetch_members():
            if roles['高三'] in member.roles:
                await member.remove_roles(roles['高三'])
                await member.add_roles(roles['已畢業'])
            elif roles['高二'] in member.roles:
                await member.remove_roles(roles['高二'])
                await member.add_roles(roles['高三'])
            elif roles['高一'] in member.roles:
                await member.remove_roles(roles['高一'])
                await member.add_roles(roles['高二'])

@bot.event
async def on_ready():
    print(f'{bot.user} 已上線！')
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_roles, CronTrigger(month=7, day=1))
    scheduler.start()

bot.run(TOKEN)
