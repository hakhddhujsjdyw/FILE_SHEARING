from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 𝑴𝒚 𝑵𝒂𝒎𝒆 : <a href=https://t.me/{}>{}</a></b>\n\n<b>📝 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆 : <a href='https://t.me/+Ou3rqTttBbJmOTA1'>𝑷𝒚𝒕𝒉𝒐𝒏</a></b>\n\n<b>📚 𝑭𝒓𝒂𝒎𝒆𝒘𝒐𝒓𝒌 : <a href='https://t.me/+UtYVAU57YVIxNThl'>𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎</a></b>\n\n<b>📡 𝑯𝒐𝒔𝒕𝒆𝒅 𝑶𝒏 : <a href='https://t.me/+1YiWOavPrhc0NmI1'>𝑯𝒆𝒓𝒌𝒖𝒐</a></b>\n\n<b>👨‍💻 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 : <a href='https://t.me/ARAKAL_THERAVAD_MOVIES_02_bot'>𝑵𝒂𝒛𝒓𝒊𝒚𝒂</a></b>\n\n<b>👥 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 : <a href='https://t.me/+FAa3tYIjXYcyZDY1'>𝑨𝑻𝑴</a></b>\n\n<b>📢 𝑼𝒑𝒅𝒂𝒕𝒆 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 : <a href='https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS'>𝑨𝑻𝑴 𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⟸ Bᴀᴄᴋ", callback_data="start"),
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


