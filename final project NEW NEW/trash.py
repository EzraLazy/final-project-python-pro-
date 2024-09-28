import discord
from discord.ext import commands
import os
import requests
import random


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('plastic'))
    with open(f'plastic/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Ini adalah contoh meme")

@bot.command()
async def glass(ctx):
    img_name = random.choice(os.listdir('glass'))
    with open(f'glass/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Gelas adalah sampah yang tajam dan bahaya, orang membuang gelas saat pecah atau tidak bagus.")

@bot.command()
async def plastic(ctx):
    img_name = random.choice(os.listdir('plastic'))
    with open(f'plastic/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Plastik adalah sampah sangat digunakan untuk membuat botol, kreasi dan lain-lain, Orang membuang plastik saat robek.")

@bot.command()
async def organic(ctx):
    img_name = random.choice(os.listdir('organic'))
    with open(f'organic/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Sampah organic adalah sampah sisa makanan atau makanan busuk seperti jagung atau ikan.")

@bot.command()
async def paper(ctx):
    img_name = random.choice(os.listdir('paper'))
    with open(f'paper/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Kertas adalah sampah yang sering digunakan untuk menulis sesuatu dan dibuang kalau dirobek.")

@bot.command()
async def metal(ctx):
    img_name = random.choice(os.listdir('metal'))
    with open(f'metal/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Metal adalah sampah yang dipakai untuk membuat banyak barang seperti alat dapur, kreasi dan lain-lain.")

@bot.command()
async def ewaste(ctx):
    img_name = random.choice(os.listdir('ewaste'))
    with open(f'ewaste/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("E-Waste adalah sampah dari electronic seperti Pc, phone, kipas dan banyak lain.")

    if ctx.content.startswith("bye"):
        await ctx.channel.send("bye!")
    if ctx.content.startswith('hi'):
        await ctx.channel.send("halo")
    else:
        await ctx.channel.send(ctx.content)


bot.run("MTI4OTQ4MTY4OTM4NjU4MjA2OA.G_4fjj.wpOjM01NDWAgzq7BnK6Qaxm7CTBYH5GR7HvnFM")