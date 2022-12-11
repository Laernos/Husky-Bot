import discord
from discord.ext import commands 
from discord import app_commands

class GC(commands.Cog):
    
    def __init__(self, bot: commands.Bot) ->None:
        self.bot = bot


    async def on_app_command_error(error: app_commands.AppCommandError, interaction: discord.Interaction):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(error, ephemeral=True)

   #-------------------------------------------------------------------------------------------------------------------------------------------            
   # SAY COMMAND (SLASH)
    @app_commands.command(name="say", description='Bot types what you typed')
    @app_commands.describe(text_to_send="Simon says this..")
    @app_commands.rename(text_to_send="message")
    async def say(self, interaction: discord.Interaction, text_to_send : str):
        await interaction.response.send_message(f"{text_to_send}", ephemeral=True)

   #-------------------------------------------------------------------------------------------------------------------------------------------         
   # HUSKIES COMMAND (SLASH)
    @app_commands.command(name= 'huskies', description='Shows member count')
    async def huskies(self, interaction: discord.Interaction):
        member_count= len(interaction.guild.members)
        guild_icon= interaction.guild.icon
        guild_name= interaction.guild.name
        embed=discord.Embed(title="", description=(f"**There are {member_count} people in this server.** "), color=0xff0000)
        embed.set_author(name=guild_name, icon_url= guild_icon)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
   #-------------------------------------------------------------------------------------------------------------------------------------------         
   # AVATAR COMMAND (SLASH)
    @app_commands.command(name="avatar", description='Gives you mentioned user\'s avatar')
    @app_commands.describe(member="@user/ID")
    async def say(self, interaction: discord.Interaction, member: discord.Member = None):
        if member == None:
            member= interaction.user

        embed=discord.Embed(title="Avatar", description="", color=0xff0000)
        embed.set_image(url= member.avatar)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    #-------------------------------------------------------------------------------------------------------------------------------------------         
    # AVATAR COMMAND (HYBRID)
    @commands.hybrid_command(name='ava', description= 'avatar')
    @commands.has_permissions(administrator = True)
    @app_commands.describe(member="@user/ID")
    @commands.cooldown(1,5)
    async def say(self, ctx:commands.context, member: discord.Member = None):
        if member == None:
            member= ctx.author
        embed=discord.Embed(title="Avatar", description="", color=0xff0000)
        embed.set_image(url= member.avatar)
        await ctx.defer(ephemeral= True)
        await ctx.reply(embed=embed, delete_after=20.0)




async def setup(bot):
    await bot.add_cog(GC(bot))