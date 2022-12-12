import discord
from discord.ext import commands
from discord import app_commands


class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel
        if channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"I have put `{channel.name}` on lockdown.")
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = None
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"I have removed `{channel.name}` from lockdown.")

    

async def setup(bot):
    await bot.add_cog(Lock(bot))