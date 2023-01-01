import discord
from discord.ext import commands
from discord import app_commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name= 'welcome')
    async def welcome(self,ctx:commands.Context):
        await ctx.send('You are missing subcommand!')    


    @welcome.group(name= 'enable')
    async def enable(self, ctx:commands.Context):

        try:
            a=await self.bot.server_config.find_field_value(ctx.guild.id,'modules', 'welcome', 'status')  
            if a is True:
                await ctx.send(f'welcome is already enabled!')
            else:
                await self.bot.server_config.update_field_value(ctx.guild.id, 'modules','welcome', 'status', True)
                await ctx.send('welcome is succesfully enabled!')                
        except KeyError:
                channel = ctx.guild.system_channel or ctx.message.channel
                data ={'status':True,'channel':channel.id, 'message':''}
                user_file= {f'modules.welcome':data}
                await self.bot.server_config.update_dc(ctx.guild.id, user_file)
                await ctx.send('welcome module is succesfully enabled.')
                if ctx.guild.system_channel is None:
                    await ctx.send(f'The welcome message channel has been set to <#{ctx.message.channel.id}>. If you like to change the channel use `!test channel <channel.id>`') 


    @welcome.group(name= 'disable')
    async def disable(self,ctx: commands.Context):
        try:
            a=await self.bot.server_config.find_field_value(ctx.guild.id,'modules', 'welcome','status')
            if a is True:
                await self.bot.server_config.update_field_value(ctx.guild.id, 'modules','welcome', 'status', False)
                await ctx.send('welcome is succesfully disabled')
            else:
                await ctx.send(f'welcome is already disabled')
        except KeyError:
            await ctx.send('welcome is already disabled!')



    @welcome.group(name= 'message')
    async def message(self,ctx: commands.Context, *,message:str):
        try:
            a=await self.bot.server_config.find_field_value(ctx.guild.id,'modules', 'welcome','status')
            if a is True:
                await self.bot.server_config.update_field_value(ctx.guild.id,'modules', 'welcome', 'message', message)
                await ctx.send(f'Welcome message has been set to `{message}`')
            else:
                await ctx.send('Welcome is not enabled. Use `!welcome enable`')                      
        except KeyError:
            await ctx.send('Welcome is not enabled. Use `!welcome enable`')  

    @welcome.group(name= 'channel')
    async def channel(self,ctx: commands.Context, channel:str):
        try:
            a=await self.bot.server_config.find_field_value(ctx.guild.id,'modules', 'welcome','status')
            if a is True:
                await self.bot.server_config.update_field_value(ctx.guild.id,'modules', 'welcome', 'channel', channel)
                await ctx.send(f'Welcome channel has been set to `{channel}`')
            else:
                await ctx.send('Welcome is not enabled. Use `!welcome enable`')                      
        except KeyError:
            await ctx.send('Welcome is not enabled. Use `!welcome enable`')  


    

async def setup(bot):
    await bot.add_cog(Welcome(bot))