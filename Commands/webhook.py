import discord
from discord.ext import commands
from discord import app_commands
from discord import Webhook
import aiohttp

class Webhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def foo(self, webhook):
        async with aiohttp.ClientSession() as session:
            embed= discord.Embed(
                title= f'{webhook.guild} banned: {webhook}',
                description='asd')
            embed.set_thumbnail(url='https://imgur.com/pH00Lsc.png')
            webhook = discord.Webhook.from_url('https://discord.com/api/webhooks/1055188080354672640/AgKGR3Mw271cf4laJqnZg_ZijhkvJkYbVQXq1KjPjhlq13tWwC5sfd_G_e2dOe6bw89_', session=session)
            await webhook.send(embed=embed, username='Foo')




    

async def setup(bot):
    await bot.add_cog(Webhook(bot))