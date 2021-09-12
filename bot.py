from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message

from_chat = -1001211588305
to_chat = -1001593777052

bot = Client("AQB_bqP9O7TE1Si3lHefMpofUsk0eo8azfva_X4fU0yu1KG0J0rX1q8y78fd5Z28LpBNdkEBMrLY5z-eST29KL6oUyHf5jP6ZfsJurlKTolPPTeFO7NePQiK4oP-IgDCqhNJNGx78U9R-icuWjXcLzwOElnI6o0XZdCzcvXYbhxoysMDuDFe51myi2oT27FfAeaLteMJb4rqbN-RFRDhN4Xd4WX1Iaga6jNxEhM-ASqVNOuxt_GqDQGbgkLkNf5m8JLjtrLUz8Hyhjbf9l-Cbp0_401j4K0w5_bFDodGJ0c-52ojhi4ISG2MJtI8yCQpxpOyyhKbKwnaRTzxXde4q9TZdjKuqQA",
      api_id=7259974,
      api_hash="bc262c77441e719e3cfc2eb61a948e7f")
    
@bot.on_message(filters.command("copy", ".")    
def copy_msg(client, message):
    m = message.reply("__Checking The Files...__")
    for ids in bot.search_messages(chat_id=from_chat", filter="empty"):
        msg_id = ids.message_id
        idss.append(msg_id)
        bot.copy_message(chat_id=to_chat, from_chat_id=from_chat, message_id=msg_id)

    else:
        if len(idss) == 0:
            m.edit("__No Files To Copy...__")
            return

        else:
            c = len(idss)
            m.edit("__Copied {c} Messages To Channel__")
            idss.clear() 

bot.run()
