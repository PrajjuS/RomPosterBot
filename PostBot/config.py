import os
from dotenv import load_dotenv

load_dotenv("config.env", override=True)

def getConfig(config_name: str):
    return os.environ.get(config_name)

try:
    BOT_TOKEN = getConfig("BOT_TOKEN")
    CHAT_ID = {int(x) for x in getConfig("CHAT_ID").split(" ")}
    WITH_BUTTONS = getConfig("WITH_BUTTONS")
    BRAND = getConfig("BRAND")
    DEVICE_NAME = getConfig("DEVICE_NAME")
    CODENAME = getConfig("CODENAME")
    MAINTAINER_USERNAME = getConfig("MAINTAINER_USERNAME")
    SUPPORT_GROUP = getConfig("SUPPORT_GROUP")
    ROM_NAME = getConfig("ROM_NAME")
    BANNER_URL = getConfig("BANNER_URL")
    ROM_VERSION = getConfig("ROM_VERSION")
    ANDROID_VERSION = getConfig("ANDROID_VERSION")
    SOURCE_CHANGELOG_URL = getConfig("SOURCE_CHANGELOG_URL")
    BUILD_DATE = getConfig("BUILD_DATE")
    BUILD_TYPE = getConfig("BUILD_TYPE")
    XDA_POST = getConfig("XDA_POST")
    DOWNLOAD_URL = getConfig("DOWNLOAD_URL")
    SCREENSHOT_URL = getConfig("SCREENSHOT_URL")
    MD5 = getConfig("MD5")
    HASHTAGS = getConfig("HASHTAGS")
except KeyError:
    print("Fill all the configs plox..\nExiting...")
    exit(0)

try:
    STICKER_ID = getConfig("STICKER_ID")
    CUSTOM_MESSAGE = getConfig("CUSTOM_MESSAGE")
except:
    pass

def check():
    if WITH_BUTTONS == "True":
        pass
    elif WITH_BUTTONS == "False":
        pass
    else:
        msg = "Config WITH_BUTTONS should be 'True' or 'False' and not anything other than these"
        msg += "\nExiting..."
        print(msg)
        exit
check()

def changelog(): # Not gonna remove this for now. I may need this in future.
    with open("changelog.txt", "r") as changelog:
        DEVICE_CHANGELOG = changelog.read()
    return DEVICE_CHANGELOG

def notes(): # Not gonna remove this for now. I may need this in future.
    with open("notes.txt", "r") as notes:
        DEVICE_NOTES = notes.read()
    return DEVICE_NOTES

def tg_format(content):
    with open(content, "r") as tg:
        TG_FORMATTED = ""
        for lines in tg.readlines():
            TG_FORMATTED = TG_FORMATTED + lines.strip("\n") + "<br>"
    return TG_FORMATTED
