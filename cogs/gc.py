import discord
from discord.ext import commands 
from discord import app_commands

class Test2(commands.Cog):
    
    def __init__(self, bot: commands.Bot) ->None:
        self.bot = bot
        
    @commands.command()
    async def test2(self, ctx, *, member: discord.Member):
        await ctx.send(f"Helllllo {member.name}")
    
    @app_commands.command(name="command1")
    async def my_command(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello from command 1!", ephemeral=True)
   
    @app_commands.command(name="alper")
    @app_commands.describe(text_to_send="Simon says this..")
    @app_commands.rename(text_to_send="message")
    async def alper(self, interaction: discord.Interaction, text_to_send : str):
        await interaction.response.send_message(f"{text_to_send}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Test2(bot))