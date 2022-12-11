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
            webhook = discord.Webhook.from_url('https://discord.com/api/webhooks/1051253592377536653/IkOMr96XHIiJg8jTvslnzs_CzoFjdv100A1OQfAiccm37EIkwJNh_z78ZsAYWFWtezf5', session=session)
            await webhook.send('Hello World', username='Foo')




    

async def setup(bot):
    await bot.add_cog(Webhook(bot))