import discord
from discord.ext import commands 
from discord import app_commands
import platform #for stats


class GC(commands.Cog):
    
    def __init__(self, bot: commands.Bot) ->None:
        self.bot = bot


    async def on_app_command_error(error: app_commands.AppCommandError, interaction: discord.Interaction):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(error, ephemeral=True)


        
   # HUSKIES COMMAND (SLASH)
    @app_commands.command(name= 'huskies', description='Shows member count')
    async def huskies(self, interaction: discord.Interaction):
        member_count= len(interaction.guild.members)
        guild_icon= interaction.guild.icon
        guild_name= interaction.guild.name
        embed=discord.Embed(title="", description=(f"**There are {member_count} people in this server.** "), color=0xff0000)
        embed.set_author(name=guild_name, icon_url= guild_icon)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
         
   # AVATAR COMMAND (SLASH)
    @app_commands.command(name="avatar", description='Gives you mentioned user\'s avatar')
    @app_commands.describe(member="@user/ID")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        embed=discord.Embed(title="Avatar", description="", color=0xff0000)
        embed.set_image(url= member.avatar)
        await interaction.response.send_message(embed=embed, ephemeral=True)
       







async def setup(bot):
    await bot.add_cog(GC(bot))