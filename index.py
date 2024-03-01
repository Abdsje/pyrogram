from pyrogram import Client, Filters

# التوكن الذي حصلت عليه من @botfather
# مثال :
# app = Client("bot", bot_token="1234567:ABCDEFGLLLL44GNVCCC")
bot = Client("bot ", bot_token="6856496719:AAE_RRi86f-wuUml7h3OgcNi9a8oIwciHOU")

# اذا كانت الرسالة في الخاص و كانت الرسالة الامر /start
@bot.on_message(Filters.private & Filters.command('start'))
def startmsg(client, message):
    # البوت سيقوم بالرد عليك بهذه الرسالة
    message.reply("اهلا بك في بوت عالم البرمجة")


bot.run() # لتشغيل البوت "long-polling
