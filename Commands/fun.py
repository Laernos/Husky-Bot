import discord
from discord.ext import commands
from discord import app_commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rockpaperscissors(self, ctx, choice: str):
        choices = ['rock', 'paper', 'scissors']
        bot_choice = random.choice(choices)
        user_choice = choice.lower()

        if user_choice not in choices:
            await ctx.channel.send('That is not a valid choice! Please choose either rock, paper, or scissors.')

        elif user_choice == bot_choice:
            await ctx.channel.send(f"It's a tie! You both chose {user_choice}.")

        elif (user_choice == 'rock' and bot_choice == 'scissors') or (user_choice == 'paper' and bot_choice == 'rock') or (user_choice == 'scissors' and bot_choice == 'paper'):
            await ctx.channel.send(f"You win! {user_choice} beats {bot_choice}.")
        else:
            await ctx.channel.send(f"You lose! {bot_choice} beats {user_choice}.")


    @commands.command()
    async def guess(self,ctx, guess: int):
        # Generate a random number between 1 and 10
        number = random.randint(1, 10)

        # Check if the guess is correct
        if 0 < guess <= 10:
            if guess == number:
                await ctx.send("Congratulations, you guessed the correct number!")
            else:
                await ctx.send(f"Sorry, the correct number was {number}.")
        else:
            await ctx.send(f'Guess must be between 1 and 10!')                    
    

    @commands.command()
    async def slot(self,ctx, bet: int):
        # Define the possible symbols and their corresponding payouts
        symbols = [
            ('🍎', 2),
            ('🍊', 2),
            ('🍇', 3),
            ('🍒', 4),
            ('🍉', 5),
            ('🍑', 6),
            ('🍋', 7),
            ('💎', 10),
            ('💰', 20),
            ('🎰', 50),
            ('💥', 100),
            ('🎉', 500),
            ('🎊', 1000),
            ('🎁', 5000),
        ]
        # Generate three random symbols
        results = [random.choice(symbols) for _ in range(3)]
        # Calculate the payout based on the symbols and the bet
        payout = sum(payout for symbol, payout in results) * bet

        embed = discord.Embed(title='🎰 Slot Machine', color=discord.Color.blue())
        embed.add_field(name='Result:', value=' '.join(symbol for symbol, _ in results))
        if payout > 0:
            embed.add_field(name='Payout:', value=f'{payout} credits')
        else:
            embed.add_field(name='Payout:', value='0 credits')
        await ctx.send(embed=embed)


    @commands.command()
    async def roll(self, ctx, num_dice: int, num_sides: int):
        # Ensure that the number of dice and sides are positive integers
        if num_dice < 1 or num_sides < 2:
            return await ctx.send('Please specify a positive number of dice and a number of sides greater than 1.')

        # Roll the dice and sum the results
        results = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(results)

        # Create an embed object with the results
        embed = discord.Embed(title='🎲 Roll the Dice', color=discord.Color.blue())
        embed.add_field(name='Results:', value=', '.join(str(result) for result in results))
        embed.add_field(name='Total:', value=total)
        await ctx.send(embed=embed)


    @commands.command()
    async def dropout_chance(self,ctx):
        chances = random.randint(0, 100)
        await ctx.send(f'There is a {chances}% chance that you will drop out of college.')



        

async def setup(bot):
    await bot.add_cog(Fun(bot))