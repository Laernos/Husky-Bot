import discord
from discord.ext import commands
from discord import app_commands, ui
from datetime import datetime


class ReasonMessage(discord.ui.Modal):
    def __init__(self, message:discord.Message):
        self.message = message
        super().__init__(title=f'Report Message')
    reason = ui.TextInput(label='Reason', style=discord.TextStyle.short, placeholder='Please provide a reason for the report')

    async def on_submit(self, interaction:discord.Interaction):
        b=await interaction.client.server_config.find_field_value(self.message.guild.id, 'modules', 'report', 'channel')
        channel=interaction.client.get_channel(int(b))
        await interaction.response.send_message('The message has been reported to the moderators!', ephemeral=True)
        embed=discord.Embed(
            title= f'❯ Reported in channel: {self.message.channel.name}',
            description=f'[{self.message.content}]({self.message.jump_url})\nReason: {self.reason.value}', 
            timestamp= datetime.now())
        embed.add_field(name='❯Reporter',value=interaction.user.mention)
        embed.add_field(name='❯Author', value=self.message.author.mention)
        await channel.send(embed=embed)


class ReasonMember(discord.ui.Modal):
    def __init__(self, member:discord.Member):
        self.member = member
        super().__init__(title=f'Report Member')
    reason = ui.TextInput(label='Reason', style=discord.TextStyle.short, placeholder='Please provide a reason for the report')

    async def on_submit(self, interaction:discord.Interaction):
        b=await interaction.client.server_config.find_field_value(self.member.guild.id, 'modules', 'report', 'channel')
        channel=interaction.client.get_channel(int(b))
        await interaction.response.send_message('The member has been reported to the moderators!', ephemeral=True)
        embed=discord.Embed(
            title= f'❯ A user has been reported',
            description='', 
            timestamp= datetime.now())
        embed.add_field(name='❯Reporter',value=interaction.user.mention)
        embed.add_field(name='❯Member', value= self.member.mention)
        embed.add_field(name='❯Reason', value= self.reason)        
        await channel.send(embed=embed)



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
            a=await self.bot.server_config.find_field_value(message.guild.id,'modules', 'report', 'status')
            if a is True:
                await interaction.response.send_modal(ReasonMessage(message))
            else:
                await interaction.response.send_message(f'Report module is disabled!', ephemeral=True)  
        except:
            await interaction.response.send_message(f'Report module has not been enabled!', ephemeral=True)        
        
    @app_commands.checks.has_permissions(ban_members=True)
    async def ReportMember_context_menu(self, interaction: discord.Interaction, member: discord.Member) -> None:    
        try:
            a=await self.bot.server_config.find_field_value(member.guild.id,'modules', 'report', 'status')
            if a is True:
                await interaction.response.send_modal(ReasonMember(member))
            else:
                await interaction.response.send_message(f'Report module is disabled!', ephemeral=True)  
        except KeyError:
            await interaction.response.send_message(f'Report module has not been enabled', ephemeral=True)      
async def setup(bot):
    await bot.add_cog(Report(bot))