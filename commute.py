import discord

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('★표시될 게임이름★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!출근"):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0x80E12A)
                channel = 751501707019812904
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='출퇴근 알람 !', value='엔진이 출근 !.')
                embed.set_image(url="https://cdn.discordapp.com/avatars/734928774528892978/fc44d14d23bc8c2ca046b35d4fafda7a.png?size=512")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("!퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0xFF0000)
                channel = 751501707019812904
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='출퇴근 알람 !', value='엔진이 퇴근 !.')
                embed.set_image(url="https://cdn.discordapp.com/avatars/734928774528892978/fc44d14d23bc8c2ca046b35d4fafda7a.png?size=512")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

client.run('NzQ4NDczODIzMzcxODUzODU0.X0d8kQ.2lLmVOlXI-lbETHfPWeWiOb9XeI')
