import discord
from discord.ext import commands
import asyncio
import random
import logging
import json
import os
import sys
import re
import logging
import urllib.request
import json
import contextlib
import re
import webbrowser
from datetime import timedelta
from discord import utils
from discord.voice_client import VoiceClient
from discord.ext.commands.bot import _get_variable
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix=('!'))


@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print("Alpha 1.0")
        print('------')
        await enter()

async def enter():
        await bot.wait_until_ready()
        await bot.change_status(game=discord.Game(name='Back to the Future'))
        
async def on_error(ctx):
        aut = ctx.message.author
        await bot.say(aut.mention + "Fuck! I ran into an error!")
        

@bot.event
async def on_member_join(member):
    await bot.wait_until_ready()
    await bot.send_message(member.server, "Welcome to the server " + member.mention + "!")
    await bot.send_message(member.server, "Use !commands to see what I can do for you!")
    
@bot.event
async def on_message(message):
        ekko = random.randint(1,14)
        if(message.content == "ding"):
                await bot.send_message(message.channel, "dong")
        elif (message.content == "!Ekko"):
                if(ekko == 1):
                        await bot.send_message(message.channel,"{0}, It's not how much time you have, it's how you use it".format(message.author.mention))
                if(ekko == 2):
                        await bot.send_message(message.channel,"Welcome to Zaun!")
                if(ekko == 3):
                        await bot.send_message(message.channel,"Someone's day's about to get wrecked.")
                if(ekko == 4):
                        await bot.send_message(message.channel,"Time to start some trouble.")
                if(ekko == 5):
                        await bot.send_message(message.channel,"Ah.. that fresh start smell.")
                if(ekko == 6):
                        await bot.send_message(message.channel,"Someone's day's about to get wrecked!")
                if(ekko == 7):
                        await bot.send_message(message.channel,"We'll do it the hard way!")
                if(ekko == 8):
                        await bot.send_message(message.channel,"I could make this hurt less")
                if(ekko == 9):
                        await bot.send_message(message.channel,"Make me repeat myself!")
                if(ekko == 10):
                        await bot.send_message(message.channel,"Time is not on your side")
                if(ekko == 11):
                        await bot.send_message(message.channel,"Should've walked away..")
                if(ekko == 12):
                        await bot.send_message(message.channel,"I like HITTING you!")
                if(ekko == 13):
                        await bot.send_message(message.channel,"Good a time to as any to act reckless")
                if(ekko == 14):
                        await bot.send_message(message.channel,"Come on! Show me something new!")

        await bot.process_commands(message)

@bot.command(pass_context=True)
async def test():
        url ="http://champion.gg/champion/Ahri"
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url,headers=hdr)
        page = urllib.request.urlopen(req)
        soup = BeautifulSoup(page,  "html.parser")
        msg = await bot.say("Getting a build")
        links = soup.findAll('img', src=True)
        for link in links:
                await bot.say("http:" + link['src'])


@bot.command(pass_context=True)
async def check(ctx):
        aut = ctx.message.author
        channel = ctx.message.channel
        bRole = utils.find( lambda r: r.name == "BotCom", channel.server.roles)
        if bRole in aut.roles:
                await bot.say("Hi " + aut.mention)
                print("Hi")
        else:
                print("No")


 
@bot.command(pass_context=True)
async def botrole(ctx):
        aut = ctx.message.author
        channel = ctx.message.channel
        await bot.say( aut.mention + "Please enter the server's id. Notice that only the server owner will be able to do this!")
        serv = await bot.wait_for_message(timeout = 120, author=aut, channel=channel)
        serv = serv.server
        roleName = 'BotCom'
        await bot.create_role(serv)
        nRole = utils.find( lambda r: r.name == "new role", channel.server.roles)
        await bot.edit_role(serv, nRole, name=roleName, hoist= True)
        await bot.say(aut.mention + "Role Created!")
        await bot.say(aut.mention + "The server owner will now be able to grant exclusive access to some of my special commands by adding the person to the new BotCom Role!"+"\n" + "Remember to pimp out the role and place other exclusive permissions if desired!")
@asyncio.coroutine
def logout():
         yield from bot.close()
         bot._is_logged_in.clear()
         
@bot.command(pass_context=True)
async def info(ctx):
        aut = ctx.message.author
        await bot.say(aut.mention + " Version Alpha 1.0 : " + "\n" + " Basic Commands and Beginning of Champ Builds")

@bot.command(pass_context=True)
async def commands(ctx):
        aut = ctx.message.author
        await bot.say(aut.mention + " PMing you the Commands list!")
        file = r".\commands.txt"
        with open(file,'r') as text_file:
                       dank = text_file.read()
                       await bot.start_private_message(aut)
                       await bot.send_message(aut, dank)

@bot.command(pass_context=True)
async def shutdown(ctx):
    aut = ctx.message.author
    channel = ctx.message.channel
    bRole = utils.find( lambda r: r.name == "BotCom", channel.server.roles)
    if bRole in aut.roles:
                await bot.say(aut.mention + "Cya, notice the bot will have to be restarted from the owner's computer... this will also turn me off on other discord servers!")
                await bot.say(aut.mention + "if there is a bug please type: bug, then state the problem. If not just type anything")
                bug = await bot.wait_for_message(timeout=60,author=aut, channel=channel)
                if bug.content == "bug":
                                        await bot.say(aut.mention + "Please state the issue right now!")
                                        issue = await bot.wait_for_message(timeout=60,author=aut, channel=channel)
                                        file =r".\bugs.txt"
                                        with open(file,'a') as text_file:
                                                text_file.write('\n' + "The bug or issue is " + str(issue.content))
                                        await bot.say(aut.mention + ":wave:")
                                        await bot.change_status(game=discord.Game(name='Offline, bot is broken'))
                                        await bot.say( aut.mention + "Preparing to Shut Down, abort with .abort")
                                        stop = await bot.wait_for_message(timeout=60, author=aut, channel=channel)
                                        if stop.content == ".abort":
                                                await bot.say(aut.mention + "SHUTDOWN ABORTTED!")
                                                await bot.change_status(game=discord.Game(name='Back to the Future'))
                                                return
                                        else:
                                                me = discord.User(id="152643425894662146")
                                                await bot.start_private_message(me)
                                                await bot.send_message(me, "A Server has turned me off ! Try to reconnect!")
                                                await logout()
                                                sys.exit()
         
                else:
                    await bot.say(aut.mention + ":wave:")
                    await bot.change_status(game=discord.Game(name=' I am Offline'))
                    me = discord.User(id="152643425894662146")
                    await bot.start_private_message(me)
                    await bot.send_message(me, "A Server has turned me off ! Try to reconnect!")
                    await logout()
                    sys.exit()
    else:
            await bot.say(aut.mention + "You do not have permission to use this command!")
        
    
@bot.command(pass_context=True)
async def bug(ctx):
        aut = ctx.message.author
        channel = ctx.message.channel
        await bot.say(aut.mention + "Please tell me the issue by typing it in!")
        issue = await bot.wait_for_message(timeout=60,author=aut, channel=channel)
        file =r".\bugs.txt"
        with open(file,'a') as text_file:
                                text_file.write('\n' + "The bug or issue is " + str(issue.content))
        await bot.say(aut.mention + "Thank you for your help!")

@bot.command()
async def cat():
    """Cat."""
    msg = await bot.say("Getting a cat...")
    url = "http://random.cat/meow"
    data = urllib.request.urlopen(url).read().decode('utf8')
    catStr = json.loads(data)
    await bot.edit_message(msg, catStr['file'])

@bot.command(hidden=True)
async def dog():
    """Dog."""
    msg = await bot.say("Getting a dog...")
    url = "http://random.dog/woof"
    data = urllib.request.urlopen(url).read().decode('utf8')
    await bot.edit_message(msg, "http://random.dog/{}".format(data))

@bot.command(pass_context=True)
async def builds(ctx):

                aut = ctx.message.author
                channel = ctx.message.channel
                
                await bot.say(aut.mention + " State the  full champ name and lane you would like a build for")
                
                buildChoice = await bot.wait_for_message(timeout=60, author=aut, channel=channel)

                #Ekko Builds                                                
                if buildChoice.content == "ekko mid":
                                await bot.say(aut.mention + " Preparing a build for: Ekko!")
                                fileName =r".\builds\Ekko_Mid.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                                
                elif buildChoice.content == "ekko top":
                                await bot.say(aut.mention + " Preparing a build for: Ekko Top!")
                                fileName =r".\builds\Ekko_Top.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True

                elif buildChoice.content == "ekko jungle":
                                await bot.say(aut.mention + " Preparing a build for : Ekko Jungle!")
                                fileName =r".\builds\Ekko_Jungle.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True

                #Yasuo Builds
                elif buildChoice.content == "yasuo mid":
                                await bot.say(aut.mention + " Preparing a build for : Yasuo Mid!")
                                fileName =r".\builds\Yasuo_Mid.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                        
                elif buildChoice.content == "yasuo top":
                                await bot.say(aut.mention + " Preparing a build for : Yasuo Top!")
                                fileName =r".\builds\Yasuo_Top.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                        
                elif buildChoice.content == "yasuo jungle":
                                await bot.say(aut.mention + " Preparing a build for : Yasuo Jungle!")
                                fileName =r".\builds\Yasuo_Jungle.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                #Riven Builds

                elif buildChoice.content == "riven top":
                                await bot.say(aut.mention + " Preparing a build for : Riven Top/Mid!")
                                fileName =r".\builds\Riven_Top.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                        
                elif buildChoice.content == "riven mid":
                                await bot.say(aut.mention + " Preparing a build for : Riven Top/Mid!")
                                fileName =r".\builds\Riven_Top.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True

                elif buildChoice.content == "riven jungle":
                                await bot.say(aut.mention + " Preparing a build for : Riven Jungle!")
                                fileName =r".\builds\Riven_Jungle.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                #Aurelion Sol Builds
                        
                elif buildChoice.content == "aurelion sol mid":
                                await bot.say(aut.mention + " Preparing a build for : Aurelion Sol Mid/Top!")
                                fileName =r".\builds\Sol_Mid.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                        
                elif buildChoice.content == "aurelion sol jungle":
                                await bot.say(aut.mention + " Preparing a build for : Aurelion Sol Jungle!")
                                fileName =r".\builds\Sol_Jungle.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                        
                elif buildChoice.content == "aurelion sok top":
                                await bot.say(aut.mention + " Preparing a build for : Aurelion Sol Top/Mid!")
                                fileName =r".\builds\Sol_Mid.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                #Vladimir Builds

                elif buildChoice.content == "vladimir mid":
                                await bot.say(aut.mention + " Preparing a build for : Vladimir Mid!")
                                fileName =r".\builds\Vlad_Mid.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                        
                elif buildChoice.content == "vladimir top":
                                await bot.say(aut.mention + " Preparing a build for : Vladimir Top!")
                                fileName =r".\builds\Vlad_Mid.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                #Zilean Builds
                        
                elif buildChoice.content == "zilean mid":
                                await bot.say(aut.mention + " Preparing a build for : Zilean Mid!")
                                fileName =r".\builds\Zilean_Mid.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True

                        
                elif buildChoice.content == "zilean support":
                                await bot.say(aut.mention + " Preparing a build for : Zilean Support!")
                                fileName =r".\builds\Zilean_Support.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                #Soraka Builds
                        
                elif buildChoice.content == "soraka support":
                                await bot.say(aut.mention + " Preparing a build for : Soraka Support!")
                                fileName =r".\builds\Soraka_Support.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                        
                elif buildChoice.content == "soraka ad":
                                await bot.say(aut.mention + " Preparing a build for : AD Soraka!")
                                await bot.say(aut.mention + " You understand Soraka has no ad scaling...")
                                await bot.say(aut.mention + " and is not that great... Oh well good luck!")
                                fileName =r".\builds\Soraka_AD.txt"
                                f = open(fileName,'r')
                                file_contents = f.read()
                                print(file_contents)
                                await bot.say(aut.mention + file_contents)
                                print("Build Complete!")
                                return True
                else:
                        await bot.say(aut.mention + "A build for that does not exist in my database! Or you spelled something wrong!")
                        print("Build Failed")
                        print("Missing Build is " + str(buildChoice.content))
                        file =r".\Errors.txt"
                        with open(file,'a') as text_file:
                                text_file.write('\n' + "Missing Build is " + str(buildChoice.content))
                        




bot.run("MjE3MDM0NTI2ODQzNjAwODk4.Cpuwsw.6enEptUU9FukjKWK-Ts3ZRLzmoM")
