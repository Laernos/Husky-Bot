#Third Party Libraries
import discord
from discord.ext import commands, tasks
from discord import app_commands, Activity, ActivityType, ui
from itertools import cycle
from pathlib import Path
import motor.motor_asyncio
import os
from datetime import datetime

#Local Code
import settings
from mongo import Document
import emotes


cwd = Path(__file__).parents[0]
cwd = str(cwd)

logger= settings.logging.getLogger('bot')



async def get_prefix(bot, message):
    # If dm's
    if not message.guild:
        return commands.when_mentioned_or("!")(bot, message)
    try:
        data = await bot.server_config.find(message.guild.id)
    # Make sure we have a useable prefix
        if not data or "prefix" not in data:
            return commands.when_mentioned_or("!")(bot, message)
        return commands.when_mentioned_or(data["prefix"])(bot, message)
    except:
        return commands.when_mentioned_or("!")(bot, message)

def run():
    intents= discord.Intents.all()
    bot = commands.Bot(command_prefix=get_prefix, owner_id = 344034871230070784,intents=intents,help_command=None)

    status= cycle(['!help | huskybot.net', f'{len(bot.guilds)} servers'])

    bot.muted_users= {}

    @bot.event
    async def on_ready():
        
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=" 🥳 HAPPY NEW YEAR"))
        
        bot.mongo= motor.motor_asyncio.AsyncIOMotorClient(str(settings.MONGO_TOKEN))
        bot.db= bot.mongo['database']
        bot.config = Document(bot.db, 'servers')
        bot.server_config = Document(bot.db, 'Server Configs')
        bot.user_data = Document(bot.db, 'User Data')


   


        logger.info(f'User: {bot.user} (ID: {bot.user.id})') 
        for filename in os.listdir('AdminCommands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'AdminCommands.{filename[:-3]}')
        logger.info("Admin Commands Ready! [1/3]")
        for filename in os.listdir('Commands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'Commands.{filename[:-3]}')
        logger.info("Commands Ready! [2/3]")
        for filename in os.listdir('Events'):
            if filename.endswith('.py'):
                await bot.load_extension(f'Events.{filename[:-3]}')
        logger.info("Events Ready! [3/3]")        


        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync()




 

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == '__main__':
    run()
