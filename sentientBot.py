import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = '-', help_command=None)
logNum = 1
#classFile = open("classRoles.txt", "r")
classList = []
    
def load_class_list():
    print("Opening class file")
    classFile = open("classRoles.txt", "r")
    print("Emptying classList...")
    classList.clear()
    for classItem in classFile:
        classList.append(classItem)
    classFile.close()
    
load_class_list()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
#on_reaction_add and _remove is not in this bot. Copy code below

@client.command()
async def load_classes(ctx):
    load_class_list()
    await ctx.send("Loading classes...")
    message = ""
    for classRole in classList:
        message = message + classRole
        
    await ctx.send("Class roles available to choose from: \n" + message)

@client.command()
async def hello(ctx):
    await ctx.send("Hi, " + ctx.author.name + "...")

@client.command()    
async def ping(ctx):
    await ctx.send(client.latency)
    
@client.command()
async def log(ctx, *, arg):
    global logNum
    content = ctx.message.content
    await ctx.send("Writing to the log " + str(logNum) + ": " + arg)
    logFile = open("log" + str(logNum) + ".txt", "wt")
    logFile.write(arg)
    logFile.close()
    logNum = logNum + 1
    
@client.command()
async def classes(ctx):
    message = ""
    for classRole in classList:
        message = message + classRole
        
    await ctx.send("Class roles available to choose from: \n" + message)

@client.command(aliases=['class'])
async def enroll(ctx, arg):
    role = ""
    for classRole in classList:
        if classRole == (arg + "\n"):
            role = arg
    
    if role == "":
        await ctx.send("Uhhh, I think you did something wrong... Try again?")
    else :
        chosenRole = discord.utils.get(ctx.guild.roles, name=role)
        if chosenRole in ctx.author.roles:
            await ctx.author.remove_roles(chosenRole)
            await ctx.send("You have been removed from the class: " + role)
        else:
            await ctx.author.add_roles(chosenRole)
            await ctx.send("You have been placed in the class: " + role)

client.run('NzcyNjQzMzM2MzUxNjQ1NzQ0.X59qLg.TTzTJTedu2kNP7hyQFsBNrNYtAU')