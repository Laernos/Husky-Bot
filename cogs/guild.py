import discord
from discord.ext import commands
from discord import app_commands


class Guild(commands.Cog):
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


#creates a database for the server in Server Configs
        data= {
            'name': integration.guild.name,            
            "id": integration.guild.id,
            }    
            
        db= await self.bot.server_config.find(integration.guild.id)
        if db is not None: #if server already has a db
            await self.bot.server_config.delete_db(integration.guild.id)      
        await self.bot.server_config.insert(data)           

#Deletes the database after bot removed
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.server_config.delete_db(guild.id)


async def setup(bot):
    await bot.add_cog(Guild(bot))