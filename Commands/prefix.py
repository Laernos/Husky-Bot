import discord
from discord.ext import commands
from discord import app_commands
import os 
import asyncio
import traceback


class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='prefix', description= 'Get or set the prefix for this server')
    @commands.has_permissions(administrator = True)
    @app_commands.describe(prefix="New prefix to use")
    @commands.cooldown(1,5)
    async def prefix(self, ctx:commands.context, prefix: str = None):
        
        data= {
            'name': ctx.guild.name,            
            "id": ctx.guild.id,
            }    
            
        db= await self.bot.server_config.find(ctx.guild.id)
        if db is None:    
            await self.bot.server_config.insert(data)  

        try:
            pre=await self.bot.server_config.find_document(ctx.guild.id,'prefix')
        except KeyError:
            pre='!'            
        if prefix:
            await self.bot.server_config.update_document(ctx.guild.id, 'prefix', prefix)            
            await ctx.send(f'I set the prefix of this server to `{prefix}`')
            if prefix=='!':
                await self.bot.server_config.delete_document(ctx.guild.id, 'prefix')
        else:
            await ctx.send(f'The prefix for this server is `{pre}`. To set a new prefix `{pre}prefix <prefix>`')
    

async def setup(bot):
    await bot.add_cog(Prefix(bot))