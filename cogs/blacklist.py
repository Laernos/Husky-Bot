import discord
from discord.ext import commands
from discord import app_commands
import json_loader

class ASD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.Member):
        if ctx.message.author.id == user.id:
            await ctx.send("Hey, you cannot blacklist yourself!")
            return

        data = json_loader.read_json("blacklist")
        data["blacklistedUsers"].append(user.id)
        json_loader.write_json(data, "blacklist")
        await ctx.send(f"Hey, I have blacklisted {user.name} for you.")

    @commands.command()
    @commands.is_owner()
    async def unblacklist(self, ctx, user: discord.Member):
        data = json_loader.read_json("blacklist")
        data["blacklistedUsers"].remove(user.id)
        json_loader.write_json(data, "blacklist")
        await ctx.send(f"Hey, I have unblacklisted {user.name} for you.")

    

async def setup(bot):
    await bot.add_cog(ASD(bot))