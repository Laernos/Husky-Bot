import discord
from discord.ext import commands
from discord import app_commands, utils

category_id= 1051245099436228679

class ticket_launcher(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Create a Ticket",style=discord.ButtonStyle.blurple, custom_id='ticket_button')
    async def ticket(self, interaction:discord.Interaction, button:discord.ui.Button):
        ticket= utils.get(interaction.guild.text_channels, name= f'ticket_{interaction.user.name.lower()}')
        if ticket is not None: await interaction.response.send_message(f'{interaction.user.name} You already have a ticket open at {ticket.mention}!', ephemeral=True)
        else:
            
            overwrites= {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel= True, send_messages= True, attach_files=True, embed_links=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
            }
            category = discord.utils.get(interaction.guild.categories, id = category_id)
            channel= await interaction.guild.create_text_channel(name=f'ticket_{interaction.user.name.lower()}', overwrites=overwrites, reason= f'Ticket for {interaction.user}', category=category)
            await channel.send(f'{interaction.user.mention} created a ticket!', view=main())
            await interaction.response.send_message(f'I\'ve opened a ticket for you at {channel.mention}!', ephemeral=True)
            

class confirm(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Confirm",style=discord.ButtonStyle.green, custom_id='confirm_button')
    async def confirm(self,interaction, button):
        try: await interaction.channel.delete()
        except: await interaction.response.send_message('Channel deletion failed! Make sure I have `manage_channels` permission!', ephemeral= True)
            

class main(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Close Ticket",style=discord.ButtonStyle.red, custom_id='close_button')
    async def close(self,interaction, button):
        embed= discord.Embed(title='Are you sure you want to close this ticket?', color= discord.Colour.blurple())
        await interaction.response.send_message(embed=embed, view=confirm())



class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.add_view=(ticket_launcher())
        self.add_view=(main())
        self.add_view=(confirm())
        self.ticket_mod= 1051213924067979345

    @commands.command()
    async def click(self, ctx):
        await ctx.send("This message has buttons!",view=ticket_launcher())     
     
    
    @app_commands.command(name="close", description='closes the ticket')
    async def close(self, interaction: discord.Interaction):
        if 'ticket_' in interaction.channel.name:
            embed= discord.Embed(title='Are you sure you want to close this ticket?', color= discord.Colour.blurple())
            await interaction.response.send_message(embed=embed, view=confirm())  
        else: await interaction.response.send_message('This isn\'t a ticket!', ephemeral=True)
        
    @commands.hybrid_command(name='add', description= 'adds user to the ticket')
    @app_commands.describe(member="The user you want to add to the ticket")
    @commands.cooldown(1,5)
    async def add(self, ctx:commands.context, member: discord.Member):
        if 'ticket_' in ctx.channel.name:
            await ctx.channel.set_permissions(member, view_channel=True, send_messages=True, attach_files=True)
            await ctx.reply(f'{member.mention} has been added to the ticket by {ctx.author.mention}')
        else: await ctx.reply('This isn\'t a ticket!')
    


async def setup(bot):
    await bot.add_cog(Ticket(bot))