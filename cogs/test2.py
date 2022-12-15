import discord
from discord.ext import commands
from discord import app_commands


class Test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def db(self, ctx):
        data= {
            'name': ctx.message.guild.name,            
            "id": ctx.message.guild.id,
            'prefix': '!',
            'commands':{
                'welcome_command':{
                    'channel':'asd',
                    'message':'asdsad'},
                'invite_command':{
                    'channnel': 'asdasd',
                    'roles': []}
            }}


        await self.bot.server_config.insert(data)


async def setup(bot):
    await bot.add_cog(Test2(bot))



    