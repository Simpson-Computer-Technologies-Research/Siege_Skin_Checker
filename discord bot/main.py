import discord, os
from discord.ext import commands

# // Setup the client
client = commands.Bot(
    command_prefix='!', 
    intents=discord.Intents(
        messages=True, 
        guilds=True, 
        reactions=True, 
        members=True, 
        presences=True
    )
)
client.remove_command('help')

# // Client on ready
@client.event
async def on_ready():
    print(f'Launched: {client.user.name} // {client.user.id}')

# // Load cogs
for filename in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cogs')):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded: cog.{filename[:-3]}')

# // Run discord bot
client.run('YOUR TOKEN')
