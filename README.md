# Rom Poster Bot
A simple Post Bot written in <a href='https://www.python.org'>Python</a> using <a href='https://pypi.org/project/pyTelegramBotAPI'>pyTelegramBotAPI</a> to post rom updates to telegram whenever you need.
Made by lazy peep for lazy peeps.

## How to use
### 1. Filling up config
Fork the repo and make a file named `config.env` by using `sample_config.env` and fill up all the vars
<br><br>
<b>Bot Configs</b>
- `WITH_BUTTONS`: 'True' if you want to post rom banner with buttons and 'False' if you want to post rom banner without buttons (Default is True)

<b>Main Configs</b>
- `BRAND`: Device brand name
- `DEVICE_NAME`: Device name
- `CODENAME`: Device codename
- `MAINTAINER_USERNAME`: Telegram username without @
- `SUPPORT_GROUP`: Telegram group username without @

<b>Rom Configs</b>
- `ROM_NAME`: Rom name
- `ROM_VERSION`: Rom version 
- `ANDROID_VERSION`: Rom android version
- `SOURCE_CHANGELOG_URL`: URL of rom source changelog
- `BANNER_URL`: Telegraph URL of your rom banner/photo
- `BUILD_DATE`: Rom build date
- `BUILD_TYPE`: Rom build type (Official/Unofficial)
- `XDA_POST`: XDA post URL of rom
- `DOWNLOAD_URL`: Download URL of rom
- `MD5`: MD5 checksum of rom
- `HASHTAGS`: Hashtags for rom post

<b>Optional Configs</b>
- `STICKER_ID`: Telegram sticker ID (If added, the bot first sends sticker then the rom post)
- `CUSTOM_MESSAGE`: Custom message to add at the end of rom post

### 2. Adding secrets
After filling up config go to your repo `settings > secrets > new repository secret`, then you need to add two secrets
- `BOT_TOKEN`: Telegram bot token
- `CHAT_ID`: Telegram group/channel chat ID where the rom needs to be posted(You can even add multiple chat IDs by seperating them with space, Example: `-0123456789 -69696969 -1003512356`)
<br><b>Note:</b> Bot should be added in the group/channel where the rom needs to be posted


### 3. Adding changelog and notes
After filling up repository secrets the add the following things
- Device side changelog in `changelog.txt` file
- Notes for the rom users in `notes.txt` file

### 4. Running the bot
After adding changelog and notes the last thing that remains is to run the bot. 
<br><b>We use Github Actions to run the bot</b>
-  Actions will automatically run after modifying changelog.txt and the rom will be posted
-  You can also run the bot but going to `actions > Rom Poster Bot Runner > workflow-dispatch` and tap on run
<br><b>Note:</b> After posting the bot pins the message too
