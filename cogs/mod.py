import discord
from discord.ext import commands
from discord import app_commands


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def kick(self,ctx,member:discord.Member, *, reason = None):
        await ctx.guild.kick(user=member, reason= f'{ctx.author.name}:{reason}')

        channel = self.bot.get_channel(1051654618188369931)
        embed= discord.Embed(title= f'{ctx.author.name} kicked: {member.name}', description=reason)
        await channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member, *, reason = None):
        await ctx.guild.ban(user=member, reason= f'{ctx.author.name}:{reason}')

        channel = self.bot.get_channel(1051654618188369931)
        embed= discord.Embed(title= f'{ctx.author.name} banned: {member.name}', description=reason)
        await channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self,ctx,member, *, reason = None):
        member= await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason= f'{ctx.author.name}:{reason}')

        channel = self.bot.get_channel(1051654618188369931)
        embed= discord.Embed(title= f'{ctx.author.name} unbanned: {member.name}', description=reason)
        await channel.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self,ctx,amount=15):
        await ctx.channel.purge(limit= amount+1)

        channel = self.bot.get_channel(1051654618188369931)
        embed= discord.Embed(title= f'{ctx.author.name} purged: {ctx.channel.name}', description=f'{amount} messages were cleared')
        await channel.send(embed=embed)


    

async def setup(bot):
    await bot.add_cog(Mod(bot))