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
import py_gg
import datetime as dt 
from datetime import timedelta
from collections import defaultdict
from discord import utils
from discord.voice_client import VoiceClient
from discord.ext.commands.bot import _get_variable
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)
py_gg.init("64b31aa6b110e5476cb84a4f7bea7afc")

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
async def builds(ctx):
        """ generate build for role of champ given"""
        aut= ctx.message.author
        channel = ctx.message.channel
        await bot.say(aut.mention+"Give Me the champ you want a build for! NOTICE YOU WILL GET THE MOST VIABLE BUILD FOR THE MOST VIABLE BUILD ACCORDING TO CHAMPION.GG")
        champ =  await bot.wait_for_message(timeout=60, author=aut, channel=channel)
        champ = str(champ.content)
        print(champ)
        await bot.say(aut.mention + "Now state the role of the build you would like, notice that not all roles have viable builds...")
        role = await bot.wait_for_message(timeout = 60, author = aut , channel =channel)
        role = str(role.content)
        #await bot.say(aut.mention+"Now give me the role")
        #role = await bot.wait_for_message(timeout=60, author=aut, channel=channel)
        mes  = py_gg.champion.items(champ,starting = True)
        for p in range(0,2):
                try:
                        if mes[p]["role"] == role:
                                try:
                                        gg = ""
                                        for i in range(0, len(mes[p]["items"])):
                                            gg =  gg + "http://ddragon.leagueoflegends.com/cdn/6.18.1/img/item/{}.png".format(mes[p]["items"][i]) + " "
                
                                        mes = py_gg.champion.items(champ, starting=False)
                                        gg1 = " "
                                        for i in range(0,len(mes[p]["items"])):
                                            gg1 =  gg1 + "http://ddragon.leagueoflegends.com/cdn/6.18.1/img/item/{}.png".format(mes[p]["items"][i]) + " "

                                        mes = py_gg.champion.runes(champ)
                                        gg2 = " "
                                     
                                        rem = mes[p]["runes"]
                                        for i in range(0, len(rem)):

                                                gg2 = gg2 + rem[i]["name"] + " " + "x"+ str(rem[i]["number"]) + "\n "

                                        mem = py_gg.champion.specific(champ)
                                        gg3 = " "
                                        cem = mem[p]['skills']
                                        tem = cem['highestWinPercent']
                                        for i in range(0, len(tem["order"])):
                                              gg3 = gg3 + "{}, ".format(tem["order"][i])
                                        mem = py_gg.champion.specific(champ)
                                        cem = mem[p]['masteries']
                                        tem = cem['highestWinPercent']
                                        rem = tem['masteries']
                                        gg4 = " "
                                        for i in range(0,len(rem)):
                                             gg4 = gg4 + " "+  rem[i]['tree'] + " " + str(rem[i]['total'])
                                        await bot.say(aut.mention + "Pming you the build!")
                                        await bot.start_private_message(aut)
                                        await bot.send_message(aut, "These are your starting Items" + "\n"+ gg + "\n" + "This is your standard build path, starting with the top item" +"\n" + gg1)
                                        await bot.send_message(aut, "Here is the  runes"+ "\n" + gg2 + " " + "\n"  + "Here is the skill order"+ "\n" + gg3 + " " + "\n" + "Here is the mastery spread" + "\n" + gg4)
                                except:
                                        await bot.say(aut.mention + "An Error has occured please tell me what you did now! EX. If you typed in a champ that does not exist then mention that you did and specify the champ!")
                                        issue = await bot.wait_for_message(timeout=60,author=aut, channel=channel)
                                        file =r".\Errors.txt"
                                        date = dt.date.today()
                                        with open(file,'a') as text_file:
                                                text_file.write('\n' + str(date) + " The Error is " + str(issue.content))
                                        await bot.say(aut.mention + "Thank you!")
                except:
                        print("Error")
                                
                            
 

@bot.command(pass_context=True)
async def matchup(ctx):
      """generates statistics for matchup between two given champs"""
      aut= ctx.message.author
      channel = ctx.message.channel
      await bot.say(aut.mention + "What is the first champ? (CASE SENSITIVE: FIRST LETTER OF WORD(S) HAVE TO BE CAPITAL)")
      champ1 = await bot.wait_for_message( timeout=60, author=aut,channel=channel)
      champ1 = champ1.content
      await bot.say(aut.mention + "What is the second champ? (CASE SENSITIVE: FIRST LETTER OF WORD(S) HAVE TO BE CAPITAL)")
      champ2 = await bot.wait_for_message( timeout=60, author=aut,channel=channel)
      champ2 = champ2.content
      match =  py_gg.champion.matchup(champ1,champ2)
     
      try:
              up = match[0]['games']
              po= match[0]['winRate']
              op= match[0]['statScore']
              kk=match[0]['role']
              await bot.say(aut.mention + "For the Role: " + str(kk)+ ", "+ champ1 + " has a " + str(po) + " % winrate against "+ champ2 +" in " + str(up) + " games")
              try:
                      up2 = match[1]['games']
                      po2= match[1]['winRate']
                      op2= match[1]['statScore']
                      kk2=match[1]['role']
                      await bot.say(aut.mention + "For the Role: " + str(kk2)+ ", "+ champ1 + " has a " + str(po2) + " % winrate against "+ champ2 +" in " + str(up2) + " games")
                      try:
                              up3 = match[2]['games']
                              po3= match[2]['winRate']
                              op3= match[2]['statScore']
                              kk3=match[2]['role']
                              await bot.say(aut.mention + "For the Role: " + str(kk3)+ ", "+ champ1 + " has a " + str(po3) + " % winrate against "+ champ2 +" in " + str(up3) + " games")
                              try:
                                      up4 = match[3]['games']
                                      po4= match[3]['winRate']
                                      op4= match[3]['statScore']
                                      kk4=match[3]['role']
                                      await bot.say(aut.mention + "For the Role: " + str(kk4)+ ", "+ champ1 + " has a " + str(po4) + " % winrate against "+ champ2 +" in " + str(up4) + " games")
                                      try:
                                              up5 = match[4]['games']
                                              po5= match[4]['winRate']
                                              op5= match[4]['statScore']
                                              kk5=match[4]['role']
                                              await bot.say(aut.mention + "For the Role: " + str(kk5)+ ", "+ champ1 + " has a " + str(po5) + " % winrate against "+ champ2 +" in " + str(up5) + " games")
                                      except:
                                              print("there is only four matchups")
                      
                              except:
                                      print("there is only three matchups")
                              
                      
                      except:
                              print("there is only two matchups")
                      
                      
              except:
                      print("there is only one match up")
      except:
                await bot.say(aut.mention + " " + "there are no matchups for these champs")
             
      

      

@bot.command(pass_context=True)
async def check(ctx):
        """ checks to see if user has exclusive command role"""
        aut = ctx.message.author
        channel = ctx.message.channel
        bRole = utils.find( lambda r: r.name == "EKKOBOT", channel.server.roles)
        if bRole in aut.roles:
                await bot.say("Hi " + aut.mention)
                print("Hi")
        else:
                await bot.say(" user does not have role")
                print("No")
         
                
 
@bot.command(pass_context=True)
async def botrole(ctx):
        """For creating a role for exlcusive bot commands"""
        aut = ctx.message.author
        channel = ctx.message.channel
        await bot.say( aut.mention + "Please enter the server's id. Notice that only the server owner will be able to do this!")
        serv = await bot.wait_for_message(timeout = 120, author=aut, channel=channel)
        serv = serv.server
        roleName = 'EKKOBOT'
        await bot.create_role(serv)
        nRole = utils.find( lambda r: r.name == "new role", channel.server.roles)
        await bot.edit_role(serv, nRole, name=roleName, hoist= True)
        await bot.say(aut.mention + "Role Created!")
        await bot.say(aut.mention + "The server owner will now be able to grant exclusive access to some of my special commands by adding the person to the new EKKOBOT Role!"+"\n" + "Remember to pimp out the role and place other exclusive permissions if desired!")
@asyncio.coroutine
def logout():
         yield from bot.close()
         bot._is_logged_in.clear()
         
@bot.command(pass_context=True)
async def info(ctx):
        """ Details about bot Version"""
        aut = ctx.message.author
        await bot.say(aut.mention + " Version Alpha 1.0 : " + "\n" + " Basic Commands and Beginning of Champ Builds")

@bot.command(pass_context=True)
async def commands(ctx):
        """DMs the user the detailed command list."""
        aut = ctx.message.author
        await bot.say(aut.mention + " PMing you the Commands list!")
        file = r".\commands.txt"
        with open(file,'r') as text_file:
                       dank = text_file.read()
                       await bot.start_private_message(aut)
                       await bot.send_message(aut, dank)

@bot.command(pass_context=True)
async def shutdown(ctx):
    """ Turns off bot"""
    aut = ctx.message.author
    channel = ctx.message.channel
    bRole = utils.find( lambda r: r.name == "EKKOBOT", channel.server.roles)
    if bRole in aut.roles:
                await bot.say(aut.mention + "Cya, notice the bot will have to be restarted from the owner's computer... this will also turn me off on other discord servers!")
                await bot.say(aut.mention + "if there is a bug please type: bug, then state the problem. If not just type anything")
                bug = await bot.wait_for_message(timeout=60,author=aut, channel=channel)
                if bug.content == "bug":
                                        await bot.say(aut.mention + "Please state the issue right now!")
                                        issue = await bot.wait_for_message(timeout=60,author=aut, channel=channel)
                                        file =r".\bugs.txt"
                                        date = dt.date.today()
                                        with open(file,'a') as text_file:
                                                text_file.write('\n' + str(date) + " The bug or issue is " + str(issue.content))
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
                    await bot.say(aut.mention + " :wave:")
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
        """ for reporting bugs"""
        aut = ctx.message.author
        channel = ctx.message.channel
        await bot.say(aut.mention + "Please tell me the issue by typing it in!")
        issue = await bot.wait_for_message(timeout=60,author=aut, channel=channel)
        file =r".\bugs.txt"
        date = dt.date.today()
        with open(file,'a') as text_file:
                                text_file.write('\n' + str(date) + " The bug or issue is " + str(issue.content))
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


                        




bot.run("xd")
