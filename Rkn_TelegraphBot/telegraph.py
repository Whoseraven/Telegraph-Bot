import os
from pyrogram import Client as Rkn_TelegraphBot, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file, Telegraph
from config import Config


@Rkn_TelegraphBot.on_message(filters.media & filters.private)
async def getmedia(bot, update):
    try:
        file = getattr(update, update.media.value)
        if file.file_size > 5 * 1024 * 1024:
            return await update.reply_text("sᴏʀʀʏ ᴅᴜᴅᴇ, ᴛʜɪs ʙᴏᴛ ᴅᴏᴇsɴ'ᴛ sᴜᴘᴘᴏʀᴛ ғɪʟᴇs ʟᴀʀɢᴇʀ ᴛʜᴀɴ 𝟻 ᴍʙ+")
        medianame = Config.DOWNLOAD_LOCATION + str(update.from_user.id)
        try:
            message = await update.reply(
                text="`Processing...`",
                quote=True,
                disable_web_page_preview=True
            )
            await bot.download_media(
                message=update,
                file_name=medianame
            )
            response = upload_file(medianame)  # returns ['/file/abc123.jpg']
            try:
                os.remove(medianame)
            except:
                pass
        except Exception as error:
            print(error)
            text = f"Error :- <code>{error}</code>"
            reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton('More Help', callback_data='help')]]
            )
            await message.edit_text(
                text=text,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
            return

        src = response[0]  # response is a list of strings like ['/file/abc123.jpg']
        text = f"**Link :-** `https://graph.org{src}`\n\n**𝑱𝒐𝒊𝒏 ⚡ :-** @Kirito_Bots"
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Open Link", url=f"https://graph.org{src}"),
                    InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{src}")
                ],
                [
                    InlineKeyboardButton(text="Join Updates Channel", url="https://t.me/Kirito_Bots")
                ]
            ]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=False,
            reply_markup=reply_markup
        )
    except Exception as error:
        await update.reply_text(
            text=f"Error :- <code>{error}</code>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('More Help', callback_data='help')]]
            )
        )


@Rkn_TelegraphBot.on_message(filters.text & filters.private)
async def text_handler(bot, update):
    try:
        telegraph = Telegraph()
        new_user = telegraph.create_account(short_name='1337')
        telegraph.access_token = new_user["access_token"]
        title = update.from_user.first_name
        content = update.text
        if '|' in update.text:
            content, title = update.text.split('|', 1)
        content = content.replace("\n", "<br>")
        author_url = f'https://telegram.dog/{update.from_user.username}' if update.from_user.username else None

        response = telegraph.create_page(
            title=title,
            html_content=content,
            author_name=str(update.from_user.first_name),
            author_url=author_url
        )

        await update.reply_text(f"https://graph.org/{response['path']}")

    except Exception as e:
        await update.reply_text(f"Error creating page:\n<code>{e}</code>")
