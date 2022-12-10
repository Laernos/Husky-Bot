import discord
from discord.ext import commands 

class Test2(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def test2(self, ctx, *, member: discord.Member):
        await ctx.send(f"Helllllo {member.name}")
   

async def setup(bot):
    await bot.add_cog(Test2(bot))