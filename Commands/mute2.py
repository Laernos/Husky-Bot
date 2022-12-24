import discord
from discord.ext import commands, tasks
from discord import app_commands
import re
import asyncio
from copy import deepcopy
from dateutil.relativedelta import relativedelta
import datetime

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}
        
class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for key, value in matches:
            try:
                time += time_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(
                    f"{value} is an invalid time key! h|m|s|d are valid arguments"
                )
            except ValueError:
                raise commands.BadArgument(f"{key} is not a number!")
        return round(time)           

class Mute2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mute(self,ctx, member:discord.Member = None):
        member= member or ctx.author 
        
        data ={
            'name':member.name,
            'mutedAt': datetime.datetime.now(),
            'muteDuration': '10',
            'mutedBy': ctx.author.id,
        }

        user_file= {f'users.muted.{member.id}':data}
        await self.bot.server_config.update_dc(ctx.guild.id, user_file)
        await ctx.reply('user has been muted!')



    @commands.command()
    async def unmute(self,ctx, member:discord.Member = None):
        member= member or ctx.author 

        await self.bot.server_config.delete_field_value(ctx.guild.id,'users', 'muted', member.id)
        await ctx.reply('user has been unmuted!')

        

async def setup(bot):
    await bot.add_cog(Mute2(bot))