import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


"""
A maioria dos comandos recebe "Consagrado" como prefixo, então deve-se digitar "Consagrado comando_desejado" para conseguir êxito.

COMMANDS:
O meu consagrado: o bot está pronto para servi-lo.
Say: falará tudo que estiver após "say".


SITUATIONS:
on_ready()  #Quando o bot entrar no servidor, o bot executará o código associado.
on_message(message)  #A partir de uma mensagem digitada por algum usuário, o bot executará o código associado.


HINTS:
0)
Para qualquer evento que se deseja que o bot faça, comece o código com
@client.event
async def em_que_situação_o_bot_deve_agir(parâmentros):
    codigo_de_ação_do_bot

1)
if message.content == "Mensagem a ser detectada":
    await client.send_message(message.channel, "Resposta") #Responde para a mensagem que foi detectada
    
2)
if message.content.upper().startswith("mensagem para chamar ele"):
    userID = message.author.id         #pega o id do autor da mensagem
    await client.send_message(message.channel, "<@%s> resposta" % (userID) #Responde a mensagem marcando no discord o autor dela.
"""

Client = discord.Client()
client = commands.Bot(command_prefix = "consagrado")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "O meu consagrado":
        await client.send_message(message.channel, "Ás ordens meu patrão.")
    if message.content.upper().startswith('CONSAGRADO SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[2:]))) #join fará com que " ", mostre os elementos da lista de args, separados pelo caractere em questão.
        #O índice começa em 2 para pular a parte onde diz "CONSAGRADO SAY".

client.run("<token>")
