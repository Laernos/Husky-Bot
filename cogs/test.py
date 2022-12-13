import discord
from discord.ext import commands
from discord import app_commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name= 'welcome')
    async def welcome(self,ctx: commands.Context):
        await ctx.send('You are missing subcommand!')    


    @welcome.group(name= 'enable')
    async def enable(self,ctx: commands.Context):
        if (find:=self.bot.db.server_config.find_one({'_id':str(ctx.guild.id)})):
            return await ctx.send("welcome already enabled")

        self.bot.db.server_config.insert_one({
            "_id":str(ctx.guild.id),
            "channel": None,
            "message": "welcome [user] to [guild]"
            })
        
        await ctx.send('welcome module is succesfully enabled.')

    @welcome.command(name='disable')
    async def disable(self,ctx:commands.Context):
        if not (find:=self.bot.db.server_config.find_one({'_id':str(ctx.guild.id)})):
            return await ctx.send('welcome module is already disabled!')
        self.bot.db.server_config.delete_one({'_id':str(ctx.guild.id)})
        await ctx.send('Welcome module is succesfully disabled!')  

    @welcome.command(name='message')
    async def message(self,ctx:commands.Context, *, message:str):
        if not (find:=self.bot.db.server_config.find_one({'_id':str(ctx.guild.id)})):
            return await ctx.send('Welcome module is nnot enabled!')
        self.bot.db.server_config.update_one({'_id':str(ctx.guild.id)}, {'$set': {'message':message}})        
        await ctx.send('Welcome message succesfgully updated!')

    @welcome.command(name='channel')
    async def channel(self,ctx:commands.Context, *, channel: discord.TextChannel):
        if not (find:=self.bot.db.server_config.find_one({'_id':str(ctx.guild.id)})):
            return await ctx.send('Welcome module is nnot enabled!')
        self.bot.db.server_config.update_one({'_id':str(ctx.guild.id)}, {'$set': {'channel':channel.id}})        
        await ctx.send('Channel message succesfully updated!')


async def setup(bot):
    await bot.add_cog(Test(bot))