import nextcord
from nextcord.ext import commands
from googletrans import Translator
from pytesseract import pytesseract
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract


guild_id = ###put your guild id here



token = ""### put your token here



t= Translator()

bot = commands.Bot()

@bot.event
async def on_ready():
  print("image translator ready!")

  
  
@bot.slash_command(name="translate", description="Translate Text To Hebrew")
async def translate_text(interaction: nextcord.Interaction, text):
  after_yarin_translate_it = t.translate(text, dest="he")
  await interaction.send(after_yarin_translate_it.text)
@bot.message_command(guild_ids=[guild_id])
async def hebrew(interaction: nextcord.Interaction, message: nextcord.Message):
  if len(message.attachments) == 1:

                for attachment in message.attachments:
        
                    await attachment.save("hello.png")
                d = r'hello.png'
                txt = pytesseract.image_to_string(d)
                tr = translator.translate(txt[:-1], 'he')
                await interaction.send(tr.text)

  else:
                try:
                    message_translate = translator.translate(
                        message.content, dest="he")
                    await interaction.response.send_message(message_translate.text)
                except Exception as error:
                    print(error)
bot.run(token)
