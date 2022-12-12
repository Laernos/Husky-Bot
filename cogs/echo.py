import discord
from discord.ext import commands
from discord import app_commands
import asyncio

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="echo",
        description="A simple command that repeats the users input back to them.",
    )
    async def echo(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title="Please tell me what you want me to repeat!",
            description="||This request will timeout after 1 minute||"
        )
        sent = await ctx.send(embed=embed)

        try:
            msg = await self.bot.wait_for(
                "message",
                timeout=60,
                check=lambda message: message.author == ctx.author
                                      and message.channel == ctx.channel
            )
            if msg:
                await sent.delete()
                await msg.delete()
                await ctx.send(msg.content)
        except asyncio.TimeoutError:
            await sent.delete()
            await ctx.send("Cancelling due to timeout.", delete_after=10)

    

async def setup(bot):
    await bot.add_cog(Echo(bot))