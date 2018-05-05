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
Versão: Exibirá a versão do bot. (permission only)
Admin: Informa o usuário se ele é admin.


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

3)
if message.content.upper().startswith('mensagem'):
    if message.author.id == "206829953205927938":
        #Tudo o que estiver aqui, será executado se e somente se o autor da mensagem tiver o ID específico acima.

4)
if message.content.upper().startswith('mensagem'):
    if "272529257614278656" in [role.id for role in message.author.roles]:
        #Tudo o que estiver aqui, será executado se e somente se o autor da mensagem tiver o role do ID especifico acima (admin no caso)
        
"""

Client = discord.Client()
client = commands.Bot(command_prefix = "consagrado")
version = "Consagrado v0.1.5 Sempre às ordens do patrão :cocktail: "
without_permission = "Você não tem permissão para executar esse comando! :rage: :rage: "


chat_filter = ["ENGENHEIRO", "BOLSONARO"]        # Filtro de palavras que não podem ser ditas no server

@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    contents = message.content.split(" ") # Contents é uma lista de palavras
    for word in contents:
        if word.upper() in chat_filter:
            await client.delete_message(message)
            await client.send_message(message.channel, "**HEEEY!** Não pode falar essa palavra por aqui :rage: ")
            print("Mensagem deletada")
    if message.content == "O meu consagrado":
        await client.send_message(message.channel, "Ás ordens, meu patrão. :ok_hand: :thumbsup:")
    if message.content in ["oi","Oi"]:
    	await client.send_message(message.channel,"Seja bem-vindo, meu patrão! :man_in_tuxedo:  ")
    if message.content == "@JRMensa#2312":
    	await client.send_message(message.channel, ":ata: ATA :ata:")
    if message.content in [":(",":sad:",":'("]:
    	await client.send_message(message.channel, "Não fique triste, já te trago litrão. :beer:")
    if message.content.upper().startswith('CONSAGRADO SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[2:]))) #join fará com que " ", mostre os elementos da lista de args, separados pelo caractere em questão.
        #O índice começa em 2 para pular a parte onde diz "CONSAGRADO SAY".
    if message.content.upper().startswith('CONSAGRADO VERSÃO'):
        if message.author.id == "206829953205927938":
            await client.send_message(message.channel, version)
        else:
            await client.send_message(message.channel, without_permission)
    if message.content.upper().startswith('CONSAGRADO ADMIN'):
        if "272529257614278656" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "O admin é cuck XDDDDD")
        else:
            await client.send_message(message.channel, "Tu não é admin não, sai fora cumpadi :fencer: :fencer: ")


client.run("<token>")
