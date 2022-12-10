import settings
import discord
from discord.ext import commands

logger= settings.logging.getLogger('bot')

def run():
    intents= discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id})')

        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)

        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

    @bot.command()
    async def test(ctx):
        await ctx.send('Working!')


    @bot.hybrid_command()
    async def ping(ctx):
        await ctx.send("pong")
        
    @bot.tree.command()
    async def ciao(interaction: discord.Interaction):
        await interaction.response.send_message(f"Ciao! {interaction.user.mention}", ephemeral=True)



    @bot.tree.context_menu(name="Show join date")
    async def get_joined_date(interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"Member joined: {discord.utils.format_dt(member.joined_at)} ", ephemeral=True)
  
    @bot.tree.context_menu(name="Report Message")
    async def report_message(interaction: discord.Interaction, message: discord.Message):
        await interaction.response.send_message(f"Message reported ", ephemeral=True)
    

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == '__main__':
    run()
