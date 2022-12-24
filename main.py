#Third Party Libraries
import discord
from discord.ext import commands, tasks
from discord import app_commands, Activity, ActivityType
from itertools import cycle
from pathlib import Path
import motor.motor_asyncio
import os

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

        
        bot.mongo= motor.motor_asyncio.AsyncIOMotorClient(str(settings.MONGO_TOKEN))
        bot.db= bot.mongo['database']
        bot.config = Document(bot.db, 'servers')
        bot.mutes = Document(bot.db, 'mutes')
        bot.server_config = Document(bot.db, 'Server Configs')
        bot.user_data = Document(bot.db, 'User Data')
        currentMutes = await bot.mutes.get_all()


        for mute in currentMutes:
            bot.muted_users[mute["_id"]] = mute

        change_status.start()     


        logger.info(f'User: {bot.user} (ID: {bot.user.id})') 
        for filename in os.listdir('AdminCommands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'AdminCommands.{filename[:-3]}')
        print("... Admin Commands Ready! [1/3]")
        for filename in os.listdir('Commands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'Commands.{filename[:-3]}')
        print("... Commands Ready! [2/3]")
        for filename in os.listdir('Events'):
            if filename.endswith('.py'):
                await bot.load_extension(f'Events.{filename[:-3]}')
        print("... Events Ready! [3/3]")        


        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)

    @tasks.loop(seconds=5)
    async def change_status():
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(status)))


    @bot.command()
    async def testt(ctx,):
        await ctx.send('Working!')


    @bot.hybrid_command()
    async def ping(ctx):
        await ctx.send(f"pong {bot.owner_id}, {len(bot.guilds)}", ephemeral=True)
        
    @bot.tree.command()
    async def ciao(interaction: discord.Interaction):
        await interaction.response.send_message(f"Ciao! {interaction.user.mention}", ephemeral=True)

    @bot.tree.context_menu(name="Show join date")
    async def get_joined_date(interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"Member joined: {discord.utils.format_dt(member.joined_at)} ", ephemeral=True)
  
    @bot.tree.context_menu(name="Report Message")
    async def report_message(interaction: discord.Interaction, message: discord.Message):
        await interaction.response.send_message(f"Message reported ", ephemeral=True)

    @bot.tree.context_menu(name="asd")
    async def asd(interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"Member joined: {interaction.user.status} {member.status} ", ephemeral=True)   

    @bot.tree.context_menu(name="Web Status")
    async def web_status(interaction: discord.Interaction, member: discord.Member):
        mobstatus= member.is_on_mobile()
        webstatus= member.web_status
        state= member.status        
        await interaction.response.send_message(f" Status: {state}\n Web Status: {webstatus}\n Mobil Status: {mobstatus}\n Desktop Status: {member.desktop_status}\n user: {member} ", ephemeral=True)







    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == '__main__':
    run()
