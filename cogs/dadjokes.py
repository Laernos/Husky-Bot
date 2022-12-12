import discord
from discord.ext import commands
from discord import app_commands
import settings
import aiohttp

class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="dadjoke",
        description="Send a dad joke!",
        aliases=['dadjokes']
    )
    async def dadjoke(self, ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': settings.API_KEY
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                r = r["body"][0]
                await ctx.send(f"**{r['setup']}**\n\n||{r['punchline']}||")

    

async def setup(bot):
    await bot.add_cog(API(bot))