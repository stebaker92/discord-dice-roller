import random
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.command('roll')
async def roll(ctx,*args):
    args = "".join(args)
    
    print("args is:" + str(args))
    
    # sanitize input - remove trailing spaces
    args=args.strip()

    args=args.replace(' ', '')

    if args == 'help':
        await ctx.send("`/roll` - rolls a 6 sided dice\n"\
                        "`/roll 4` - rolls a 4 sided dice\n"\
                        "`/roll 2d6` - rolls two 6-sided dice\n"\
                        )
        return
        
    diceToRoll=1
    numberOfSides=6

    if args:
        try:
            (diceToRoll,numberOfSides)=parseInput(args)
        except:
            await ctx.send('I didn''t understand your input: `' + args + '`.\n try `/roll help` for supported options')
            return
    
    await ctx.send('Rolling `' + str(diceToRoll) + '` dice with `' + str(numberOfSides) + '` sides')

    results = []
    
    for _ in range(0, diceToRoll):
        print('rolling a ' + str(numberOfSides) + ' sided dice')
        results.insert(0, '['+str(rolladice(numberOfSides))+']')

    resultString = ',  '.join(results)
    
    await ctx.send('Results: ' + resultString)

def parseInput(input):
    split=input.split('d')

    # remove empty items
    split=[x for x in split if x]

    if len(split) == 1:
        diceToRoll = 1
        sidedDice = int(split[0])
    elif len(split) == 2:
        diceToRoll = int(split[0])
        sidedDice = int(split[1])

    if diceToRoll > 99:
        raise Exception('too many dice')
    
    if sidedDice > 999:
        raise Exception('too many sides')

    return diceToRoll, sidedDice

def rolladice(sides):
    return random.randint(1, sides)

bot.run(TOKEN)
