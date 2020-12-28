import discord
import asyncio
import os

token = 'NzkxNTM5MTY3OTk3MzI5NDE4.X-QoSw.SSO22ilbCkLczalIenWfdBSMOmg'

client = discord.Client()

@client.event
async def on_ready():
    print('봇 켜졌다 주인놈아!')
    print(client.user.name + "봇")
    print(client.user.id)
    print('====================================')
    while True:
       user = len(client.users)
       server = len(client.guilds)
       messages = ["안녕하세요!", "Sturway#2482(Hestia#1234 이분도)님이 제작하신 봇" , str(user) + "명이 저와 놀고있어요!", str(server) + "개의 서버에서 안전하게 보관되고 있어요!","!도움으로 저의 명령어를 알아보세요!"]
       for (m) in range(5):
           await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.playing))
           await asyncio.sleep(3)

@client.event
async def on_message(message):
    if message.content.startswith("!도움"):
        embed=discord.Embed(title="Sturway봇의 도움말!", description="안녕하세요! Sturway봇입니다! 접두사는 ``!``입니다!", color=0x1000eb)
        embed.add_field(name="핑", value="핑을 알려줍니다!", inline=False)
        embed.add_field(name="밴 (id)", value="그 id를 가진 유저를 밴합니다!", inline=False)
        embed.add_field(name="언밴 (id)", value="그 id를 가진 유저를 언밴합니다!", inline=False)
        embed.add_field(name="청소 (메시지 수)", value="입력한만큼의 메시지를 청소합니다!", inline=False)
        embed.add_field(name="초대", value="봇의 초대링크를 드립니다!", inline=False)
        embed.set_footer(text=f"요청자:{message.author}")
        await message.channel.send(embed=embed)
    if message.content.startswith("!핑"):
        await message.channel.send ("🏓 퐁! " + str(round(client.latency * 1000)) + "ms!")
    if message.content.startswith("!밴"):
        if message.author.guild_permissions.administrator:
            user = await client.fetch_user(int(message.content[3:21]))
            await message.guild.ban(user, reason="Sturway 봇이 밴함")
        else:
            await message.channel.send(f"관리 권한 필요한데")
    if message.content.startswith("!언밴"):
        if message.author.guild_permissions.administrator:
            user = await client.fetch_user(int(message.content[4:22]))
            await message.guild.unban(user)
        else:
            await message.channel.send(f"관리 권한 필요한데")
    if message.content.startswith("!청소"):
        if message.author.guild_permissions.administrator:
            number = int(message.content.split(" ")[1])
            await message.channel.purge(limit=number)
        else:
            await message.channel.send(f"관리 권한 필요한데")
    if message.content == ("!초대"):
        await message.channel.send ("https://discord.com/api/oauth2/authorize?client_id=791539167997329418&permissions=8&scope=bot")
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

