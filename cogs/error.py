import discord
from discord.ext import commands
from discord import app_commands


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx:commands.Context, error) -> None:
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"{round(error.retry_after, 2)} seconds left")
        else:
            await ctx.reply(error, ephemeral=True)





    

async def setup(bot):
    await bot.add_cog(Error(bot))