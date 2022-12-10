import discord
from discord.ext import commands 


class Greetings(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def test2(self, ctx, *, member: discord.Member):
        await ctx.send(f"Hello {member.name}")
        
async def setup(bot):
    await bot.add_cog(Greetings(bot))