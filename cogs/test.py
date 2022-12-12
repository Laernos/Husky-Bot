import discord
from discord.ext import commands
from discord import app_commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#sents a message to the owner of the server on join!
    @commands.Cog.listener()
       
    async def on_guild_join(self,guild):
        # get all server integrations
        integrations = await guild.integrations()

        for integration in integrations:
            if isinstance(integration, discord.BotIntegration):
                if integration.application.user.name == self.bot.user.name:
                    bot_inviter = integration.user# returns a discord.User object
                    
                    # send message to the inviter to say thank you
                    await bot_inviter.send(f"Thank you for inviting {self.bot.user.name}!")
                    break

    

async def setup(bot):
    await bot.add_cog(Test(bot))