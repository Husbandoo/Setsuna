from saucenao_api import SauceNao, VideoSauce, BookSauce
from telegraph import upload_file as keko
from jikanpy import Jikan
import cv2
from saucenao_api.params import DB
import os
from SaitamaRobot import dispatcher 
from SaitamaRobot import SAUCE_API
from SaitamaRobot.modules.disable import (DisableAbleCommandHandler, DisableAbleMessageHandler) 
from SaitamaRobot.modules.helper_funcs.chat_status import (user_admin,
                                                           user_not_admin)
from telegram import (Chat, InlineKeyboardButton, InlineKeyboardMarkup,
                      ParseMode, Update)
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          Filters, MessageHandler, run_async)
from telegram.utils.helpers import mention_html








@run_async 
def sauce(update: Update, context: CallbackContext ):
  results = " "
  API = str(SAUCE_API)
  if API == "None": 
    return msg.reply_text("Sauce api not set!!")
  sauce = SauceNao(api_key=API, db = 999, numres = 6)
  bot = context.bot 
  msg = update.effective_message 
  msg_id = update.effective_message.message_id 
  chat = update.effective_chat 
  reply = msg.reply_to_message
  filename_photo = "saucey.png"
  filename_gif = "saucey.gif" 
  if not reply:
    msg.reply_text("Reply to something baka...")
    return
  photo = "False"
  gif = "False"
  m = msg.reply_text("Where is my frying pan.. Ahh!! Hot Sauce-ing now!!", reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text = "(^_-)", callback_data = "Nah")]]))
  if reply:
    if reply.photo:
      photo_id = reply.photo[-1].file_id
      photo = "True" 
    elif reply.animation:
      gif_id = reply.animation.file_id
      gif = "True" 
    elif reply.video:
      if reply.video.file_size >= 5:
        gif_id = reply.video.file_id
        gif = "True"
      else:
        m.edit_text("Ahh That is too big for setsuna, give a small sized one Nya!!")
    elif reply.sticker:
      photo_id = reply.sticker.file_id
      photo = "True" 
    else:
      m.edit_text("Nyah!!, give a gif, photo or a sticker!! ")
      return
    if photo == "True":
      file = bot.get_file(photo_id)
      dl = file.download(filename_photo)
      oo = open(dl, 'rb')
      results = sauce.from_file(oo)
      os.remove(dl)
    elif gif == "True" :
        file = bot.get_file(gif_id)
        dl = file.download(filename_gif)
        nyah = cv2.VideoCapture(dl)
        heh, nyo = nyah.read()
        cv2.imwrite("nyah.png", nyo)
        results = sauce.from_file(open("nyah.png", 'rb')) 
        nyah.release()
        os.remove(dl)
      #except Exception:
        #m.edit_text("Ahh its too big!!, Setsuna cant hanlde it Nya!")
    else:
      return
  ru = []
  rsu_1  = int(results[0].index_id) 
  rsu_2 = int(results[1].index_id)
  rsu_3 = int(results[2].index_id)
  rsu_4 = int(results[3].index_id) 
  rsu_5 = int(results[4].index_id)
  rsu_6 = int(results[5].index_id) 
  text = " "
  markup = " "
  tex_dan, url_dan, material_dan, creator_dan, source_dan, character_dan, tex_pix, mem_pix, url_pix,  anime_url, anime_title,  dan_simi, simi_pix, anime_year, anime_ep= " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "
  mal_url = "False"
  rsudan = "False"
  rsupix = "False"
  rsuAnime = "False"
  urgel = "False"
  
  if rsu_1 == 9:
    rsudan = "True"
    rsu = 0 
  elif rsu_2 == 9:
    rsudan = "True"
    rsu = 1
  elif rsu_3 == 9:
    rsudan = "True"
    rsu = 2 
  elif rsu_4 == 9:
    rsudan = "True"
    rsu = 3 
  elif rsu_5 == 9:
    rsudan = "True"
    rsu = 4 
  elif rsu_6 == 9:
    rsudan = "True"
    rsu = 5 
  else:
    print("Danboruu not found")
    
  if rsu_1 == 5:
    rsupix = "True"
    rsu2 = 0
  elif rsu_2 == 5:
    rsupix = "True"
    rsu2 = 1
  elif rsu_3 == 5:
    rsupix = "True"
    rsu2 = 2
  elif rsu_4 == 5:
    rsupix = "True"
    rsu2 = 3
  elif rsu_5 == 5:
    rsupix = "True"
    rsu2 = 4
  elif rsu_6 == 5:
    rsupix = "True"
    rsu2 = 5
  else:
    print("Pixiv not found...")
    
  if rsu_1 == 21:
    rsuAnime = "True"
    rsu3 = 0 
  elif rsu_2 == 21:
    rsuAnime = "True"
    rsu3 = 1
  elif rsu_3 == 21:
    rsuAnime = "True"
    rsu3 = 2
  elif rsu_4 == 21:
    rsuAnime = "True"
    rsu3 = 3
  elif rsu_5 == 21:
    rsuAnime = "True"
    rsu3 = 4
  elif rsu_6 == 21:
    rsuAnime = "True"
    rsu3 = 5
  else:
    print("Not found on Anime..")
    
  if rsudan == "True" :
    dan_simi = str(results[rsu].similarity)
    tex_dan = str(results[rsu].title)
    urdan = results[rsu].urls
    try:
      urgel = urdan[1]
    except IndexError:
      pass
    if len(urdan) >= 2:
      tit = urdan.pop()
    else:
      pass
    url_dan = " ".join(urdan)
    di = results[rsu].raw
    ik = di.get('data')
    if not ik == "None":
      creator_dan = ik.get('creator') 
      material_dan = ik.get('material')
      source_dan = ik.get('source')
      character_dan = ik.get('characters')
    print("Danboruu retrieving successful...")
  else:
    print("Danboruu either not found or retrieving unsuccessful")
    
  if rsuAnime == "True":
    raww = results[rsu3].raw
    anime_url = results[rsu3].urls
    try:
      anime_url = anime_url[0]
    except IndexError:
      pass 
    simi = str(results[rsu3].similarity) 
    deta = raww.get('data')
    anime_title = deta.get('source') 
    anime_ep = deta.get('part')
    anime_year = deta.get('year')
    anime_timestamp = deta.get('est_time' )
    print("Anime retrieving successful...")
    heh = Jikan()
    kek = heh.search('anime', anime_title, page=1)
    if kek:
      mal_url = kek['results'][0]['url']
    else:
      mal_url = "False"
  else:
    print("Anime not found or retrieving unsuccessful")
  
  if rsupix == "True" :
     url_pix = " ".join(results[rsu2].urls) 
     simi_pix = str(results[rsu2].similarity) 
     tex_pix = str(results[rsu2].title)
     kek = results[rsu2].raw
     ti = kek.get('data')
     if not ti == 'None':
       mem_pix = ti.get('member_name')
     pixiv = "True" 
     print("Pixiv retrieving successful...")
  else:
     print("Pixiv not found or retrieving unsuccessful")
    
  if rsuAnime == "True":
    text += f"*Title: {anime_title}\nEpisode: {anime_ep}* \n*Year Released*: `{anime_year}` \n*Timestamp:* `{anime_timestamp}`\n*Similarity:* `{simi}`"
    print(text)
    
  if rsudan == "True" :
    text += "*Title:*" + " " + f"*{tex_dan}*" + " " + "\n*Creator:*" + " " +  f"*{creator_dan}*" + "\n*Material:*" + " " + f" *{material_dan}*" + "\n*Character:*" + " " + f"*{character_dan}*" + "\n" + "*Similarity: " + " " + f"{dan_simi}*" 
    print(text)

  if rsupix == "True":
    if rsuAnime == "True":
      pass
    elif rsudan == "True":
      pass 
    else:
      text +=  "*Title:*" + " " + f"*{tex_pix}*" + "\n" +  "*Artist:*" + " " + f"*{mem_pix}*\n" + f"*Similarity: {simi_pix}*"
  
  if text == " ":
    text = "Sorry Not found!!, Setsuna sad... reeeee"
  #buttons made here 
  keybo = []
  if rsupix == "True":
    keybo.append([InlineKeyboardButton(text = "Pixiv", url = url_pix)])
  if rsudan == "True":
    if not urgel == "False":
      keybo.append([InlineKeyboardButton(text = "Danboruu", url = url_dan), InlineKeyboardButton(text = "Gelbooru", url = urgel)])
    elif url_dan == "False":
      if not urgel == "False":
        keybo.append([InlineKeyboardButton(text ="Gelbooru", url = urlgel)])
    else:
      keybo.append([InlineKeyboardButton (text = "Danboruu", url = url_dan)])
  if rsuAnime == "True":
      keybo.append([InlineKeyboardButton(text = "Anime-db", url = anime_url)])
  if not mal_url == "False":
      keybo.append([InlineKeyboardButton(text = "MAL", url = mal_url)])
  if len(keybo) >= 1:
    markup = InlineKeyboardMarkup(keybo)
    m.delete()
    msg.reply_text(text = text, reply_markup = markup, parse_mode = ParseMode.MARKDOWN)
  else:
    m.delete()
    msg.reply_text(text, parse_mode = ParseMode.MARKDOWN)
     
 
__help__ = """
*Ketchup Bottle*

Its simple, reply /sauce to any picture to get the source of the image or what anime it is..., it works 90% of the time... and will be bringing gif suace too!!! Nyah!! 

If something goes wrong please report @SetsunaBotSupport 
"""
SAUCE_HANDLER = DisableAbleCommandHandler("sauce", sauce) 
dispatcher.add_handler(SAUCE_HANDLER)
    
__mod_name__ = "Sauce"   
__command_list__ = ["sauce"]
__handlers__ = [SAUCE_HANDLER]
      