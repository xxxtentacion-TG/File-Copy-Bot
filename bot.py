from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from values import API_ID, API_HASH, SESSION, FROM_CHAT, TO_CHAT, FILE_TYPE, CAPTION
idss = []

bot = Client(SESSION,
      api_id=API_ID,
      api_hash=API_HASH)
    
@bot.on_message(filters.command("copy", "."))
def copy_msg(client, message):
    m = message.reply("__Checking The Files...__")
    try:
       for ids in bot.search_messages(chat_id=FROM_CHAT, filter=FILE_TYPE): 
           msg_id = ids.message_id
           idss.append(msg_id)
           bot.copy_message(chat_id=TO_CHAT,
                            from_chat_id=FROM_CHAT,
                            message_id=msg_id, 
                            caption=CAPTION)
       else:
           if len(idss) == 0:
               m.edit("__No Files To Copy...__")
               return
           else:
               c = len(idss)
               m.edit(f"__Copied {c} Messages To Channel__")
               idss.clear() 

    except Exception as x:
       m.edit(f"Error Occurred: {x}")

bot.run()
