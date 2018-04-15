 #Import
import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord.voice_client import VoiceClient
import os


#Vars
with open("prefix.data") as prefixf:
	prefix = prefixf.readline()
Client = discord.Client()
client = commands.Bot(command_prefix = prefix)
with open("token.data") as tokenf:
	token = tokenf.readline()

@client.command(pass_context = True)
async def play(ctx, *, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    try:
        vc = await client.join_voice_channel(voice_channel)
        msg = await client.say("Loading...")
        player = await vc.create_ytdl_player("ytsearch:" + url)
        player.start()
        await client.say("Succesfully Loaded ur song!")
        await client.delete_message(msg)
    except Exception as e:
        print(e)
        await client.say("Reconnecting")
        for x in client.voice_clients:
            if(x.server == ctx.message.server):
                await x.disconnect()
                nvc = await client.join_voice_channel(voice_channel)
                msg = await client.say("Loading...")
                player2 = await nvc.create_ytdl_player("ytsearch:" + url)
                player2.start()


@client.command(pass_context = True)
async def stop(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await client.say("I am not playing anyting???!")
@client.command(pass_context = True)
async def ping(ctx):
    client.say("POing")


@client.event
async def on_message(message):
	await client.process_commands(message)




client.run(token)
