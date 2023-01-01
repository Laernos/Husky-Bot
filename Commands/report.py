import discord
from discord.ext import commands
from discord import app_commands, ui
from datetime import datetime


class Report(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(
            name='Report Message',
            callback=self.ReportMessage_context_menu,
        )
        self.ctx_menu2 = app_commands.ContextMenu(
            name='Report Member',
            callback=self.ReportMember_context_menu,
        )        
        self.bot.tree.add_command(self.ctx_menu)
        self.bot.tree.add_command(self.ctx_menu2)

    async def cog_unload(self) -> None:
        self.bot.tree.remove_command(self.ctx_menu.name, type=self.ctx_menu.type)

    async def ReportMessage_context_menu(self, interaction: discord.Interaction, message: discord.Message) -> None:
        try:
            a=await self.bot.server_config.find_field_value(message.guild.id,'modules', 'welcome', 'status')
            if a is True:
                b=await self.bot.server_config.find_field_value(message.guild.id, 'modules', 'welcome', 'channel')
                channel=self.bot.get_channel(int(b))
                await interaction.response.send_message('The message has been reported to the moderators!', ephemeral=True)
                embed=discord.Embed(
                    title= f'❯ Reported in channel: {message.channel.name}',
                    description=f'[{message.content}]({message.jump_url})', 
                    timestamp= datetime.now())
                embed.add_field(name='❯Reporter',value=interaction.user.mention)
                embed.add_field(name='❯Author', value=message.author.mention)
                await channel.send(embed=embed)
            else:
                await interaction.response.send_message(f'Report module has not been enabled!', ephemeral=True)  
        except:
            await interaction.response.send_message(f'Report module has not been enabled!', ephemeral=True)        
        
    @app_commands.checks.has_permissions(ban_members=True)
    async def ReportMember_context_menu(self, interaction: discord.Interaction, member: discord.Member) -> None:    
        try:
            a=await self.bot.server_config.find_field_value(member.guild.id,'modules', 'welcome', 'status')
            if a is True:
                b=await self.bot.server_config.find_field_value(member.guild.id, 'modules', 'welcome', 'channel')
                channel=self.bot.get_channel(int(b))
                await interaction.response.send_message('The member has been reported to the moderators!', ephemeral=True)
                embed=discord.Embed(
                    title= f'❯ A user has been reported',
                    description='', 
                    timestamp= datetime.now())
                embed.add_field(name='❯Reporter',value=interaction.user.mention)
                embed.add_field(name='❯Member', value=member.mention)
                await channel.send(embed=embed)
            else:
                await interaction.response.send_message(f'Report module has not been enabled!', ephemeral=True)  
        except:
            await interaction.response.send_message(f'Report module has not been enabled!', ephemeral=True)      
async def setup(bot):
    await bot.add_cog(Report(bot))