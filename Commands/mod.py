import discord
from discord import File
from discord.ext import commands
from discord import app_commands
from datetime import datetime
from easy_pil import Editor, load_image_async, Font

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member, *, reason = None):
        #await ctx.guild.kick(user=member, reason= f'{ctx.author.name}:{reason}')
        embed= discord.Embed(title= f'{ctx.author.name} kicked: {member.name}', description=reason)
        await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self,ctx,members:commands.Greedy[discord.Member]=None, *, reason = None):

        for member in members: # members is a list that greedy has created
            try:
                user_image= await load_image_async(str(member.avatar))
                jail_image = await load_image_async(str('https://imgur.com/u3GEpDV.png'))
                user= Editor(user_image).resize((70,70))
                jail = Editor(jail_image).resize((70,70))
                user.paste(jail, (0,0))
                file= File(fp=user.image_bytes, filename='pic1.png')

                await ctx.guild.ban(user=member, reason= f'{ctx.author.name}#{ctx.author.discriminator}: {reason}')
                reason= f'`{reason}`'
                if reason[1:-1] == 'None': reason= '<:no_data:1055471334542553139>'
                if reason[1:-1] == '<:no_data:1055471334542553139>': reason= '<:no_data:1055471334542553139>'
                embed= discord.Embed(title= '', description=f'{member.mention} **has been banned by** {ctx.author.mention}\n**Reason:** {reason}')
                embed.set_author(name= f'{ctx.channel.guild.name} Security 🛡️', icon_url=ctx.channel.guild.icon)
                embed.set_thumbnail(url='attachment://pic1.png')        
                await ctx.channel.send(file=file, embed=embed)
            except discord.Forbidden:
                await ctx.channel.send('forbidden error')   

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self,ctx,member, *, reason = None):
        member= await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason= f'{ctx.author.name}#{ctx.author.discriminator}: {reason}')
        reason= f'`{reason}`'
        if reason[1:-1] == 'None': reason= '<:no_data:1055471334542553139>'
        embed= discord.Embed(title= '', description=f'{member.mention} **\'s ban has been lifted by** {ctx.author.mention}\n**Reason:** {reason}')
        embed.set_author(name= f'{ctx.channel.guild.name} Security 🛡️', icon_url=ctx.channel.guild.icon)        
        embed.set_thumbnail(url='https://imgur.com/EhBcoNW.png')
        await ctx.channel.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self,ctx,amount=15):
        try:
            if not ctx.author.bot: 
                await self.bot.server_config.find_field(ctx.guild.id, 'commands', 'logging_cmnd')
                if await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'message', 'status') is True:
                    b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'message', 'channel')
                    channel=self.bot.get_channel(int(b))        
                    await ctx.channel.purge(limit= amount+1)
                    embed= discord.Embed(title= f'{ctx.author.name} purged: {ctx.channel.name}', description=f'{amount} messages were cleared')
                    await channel.send(embed=embed)
        except KeyError:
            return

    

async def setup(bot):
    await bot.add_cog(Mod(bot))