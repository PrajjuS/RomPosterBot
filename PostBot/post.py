import telebot
from config import *

bot = telebot.TeleBot(f"{BOT_TOKEN}", parse_mode="HTML")

def send_post(chat_id, image, caption):
    if caption == "" or not caption or caption is None:
        return bot.send_photo(chat_id=chat_id, photo=image)
    else:
        return bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def message_content():
    msg = ""
    msg += f"<b>{ROM_NAME} {BUILD_TYPE} for {BRAND} {DEVICE_NAME} ({CODENAME})</b>\n\n"
    msg += f"<b>Maintainer:</b> @{MAINTAINER_USERNAME}\n"
    msg += f"<b>Rom Version:</b> {ROM_VERSION} <b>|</b> Android {ANDROID_VERSION}\n"
    msg += f"<b>Build Date:</b> {BUILD_DATE}\n\n"
    msg += f"<b>Source Changelogs:</b> <a href='{SOURCE_CHANGELOG_URL}'>Here</a>\n\n"
    msg += f"<b>Device Changelogs:</b>\n{changelog()}\n\n"
    msg += f"<b>Notes:</b>\n{notes()}\n\n"
    msg += f"<b>XDA Thread:</b> <a href='{XDA_POST}'>Here</a>\n"
    msg += f"<b>Download:</b> <a href='{DOWNLOAD_URL}'>Here</a>\n"
    msg += f"<b>MD5:</b> <code>{MD5}</code>\n\n"
    msg += f"<b>Support Group:</b> @{SUPPORT_GROUP}\n\n"
    if CUSTOM_MESSAGE:
        msg += f"<b>{CUSTOM_MESSAGE}</b>"
        msg += f"{HASHTAGS}"
    else:
        msg += f"{HASHTAGS}"
    return msg

def tg_message():
    if STICKER_ID:
        bot.send_sticker(CHAT_ID, STICKER_ID)
        send_post(CHAT_ID, BANNER_URL, message_content())
    else:
        send_post(CHAT_ID, BANNER_URL, message_content())

tg_message()
