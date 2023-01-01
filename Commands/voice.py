import discord
from discord.ext import commands
from discord import app_commands


class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def join(self,ctx):
        # Get the voice channel the user is in
        # Check if the user is in a voice channel
        # Join the voice channel
    

        try:
            voice_channel = ctx.message.author.voice.channel
            await voice_channel.connect()
            await ctx.send(f'Connected to voice channel {voice_channel.name}')
        except:
            await ctx.send('You are not in a voice channel!')   
        


    

    

async def setup(bot):
    await bot.add_cog(Voice(bot))