import discord
from discord.ext import commands
from discord import app_commands


        

class Db(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def resetdb(self,ctx):
        data= {
            'name': ctx.guild.name,            
            "id": ctx.guild.id,
            }    
        await self.bot.server_config.delete(ctx.guild.id)
        await self.bot.server_config.insert(data)
        await ctx.reply('> Database has been reset!')
        


   

    

async def setup(bot):
    await bot.add_cog(Db(bot))