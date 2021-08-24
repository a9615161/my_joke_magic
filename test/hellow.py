#導入 Discord.py
import discord
import os, random, shutil

#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == 'ping':
        await message.channel.send('pong')

client.run('ODc5NTYzMDkwMDUwNTQ3NzIy.YSRi9g.gYr0mmSyacIFEk8Ur_G_2Tsejjw') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
def moveFile(fileDir):
    pathDir = os.listdir(fileDir)    #取圖片的原始路徑
    filenumber=len(pathDir)
    rate=0.1    #自定義抽取圖片的比例，比方說100張抽10張，那就是0.1
    picknumber=int(filenumber*rate) #按照rate比例從資料夾中取一定數量圖片
    sample = random.sample(pathDir, picknumber)  #隨機選取picknumber數量的樣本圖片
    print (sample)
    for name in sample:
            shutil.move(fileDir+name, tarDir+name)
    return  