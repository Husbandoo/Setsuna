import random as rdm
import nekos 
from Setsuna import dispatcher
from Setsuna.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async


neko = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'gasm', 'poke', 'anal', 'hentai', 'erofeet', 'holo' 'blowjob', 'pussy', 'tits', 'holoero', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug','baka', 'woof']

@run_async
def random(update: Update, context: CallbackContext ):
    msg = update.effective_message.message_id
    bot = context.bot 
    user = update.effective_user.id
    chat = update.effective_chat.id
    kek = rdm.choice(neko)
    nek = nekos.img(kek)
    if nek.endswith("gif"):
        bot.send_animation(chat_id =chat, animation = nek, reply_to_message_id = msg )
    else:
        bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = msg)
   
RANDOM_HANDLER = DisableAbleCommandHandler("letsfap", random)
dispatcher.add_handler(RANDOM_HANDLER)
 



