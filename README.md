# Duty notifier

---

## Requirements
- [git](https://github.com/git-guides/install-git)
- [docker](https://docs.docker.com/engine/install/)

---

## Content

- [Telegram bot](#telegram-bot)
- [Table filler](#table-filler)
- [Tips](#tips)

---

## Telegram bot

### Description

Duty Notifier Bot sends automated notifications about duty schedules and work shifts to Telegram groups. It supports sending messages to regular group/multiple groups. You can also specify the time at which a message with today's work shift will be sent. The bot provides two commands: one shows the current duty officer and backup duty officer, the second displays all duty officers and backup duty officers for the current week.

### Installation
1. Download project and open required folder:

    ```
    cd /opt
    git clone https://github.com/wedunty/duty-notifier.git
    cd duty-notifier/telegram_bot
    ```

2. Configuring the bot:
    - Open .env file.

    - Put your bot's token, group(s) id, timezone and the notification time like this:
      ```
      BOT_TOKEN=0123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
      GROUPS_ID={"1'st": "xxxxxxxxxxxx", "2'nd": "xxxxxxxxxxxx", "3'rd": "xxxxxxxxxxxx", "4'th": "xxxxxxxxxxxx"}
      NOTIFY_HOUR=XX
      NOTIFY_MINUTE=XX
      TZ=your_continent/your_city
      ```
    - Open files/tables.

    - Add as many tables as you need (in the same format as the sample tables).

    - Each table must begin with what you have specified as the key to the group ID for which the table is intended.

3. Giving the bot access to messages:
    - Type /mybots in chat with @BotFather and select a bot.

    - Press "Bot Settings" --> "Group Privacy".

    - Press "Turn off".

4. Adding a list of commands:
    - Type /setcommands in chat with @BotFather and select a bot.
  
    - Type the following:
      ```
      current_attendant - {description} # This command will show you the current duty officer and his deputy
      week_attendants - {description} # This command will show you the duty officers and their deputies for the current week
      ```

5. Bot startup:
    - Go to project directory: 
    ```cd /opt/duty-notifier/telegram_bot```
    - Create an image: 
    ```docker build -t {name of your image} .```
    - Start the image: 
    ```docker run -d --env-file .env -v ./files/tables:/duty_notifier/files/tables --name {name of your container} {name of your image}```

6. After that files/tables folder will be synced with docker container and all you'll have to do is replace the tables in this folder in a timely manner.

---

## Table filler 

### Description

This script helps to create a duty table used to work with duty-notifier.

### Usage

1. Open table_filler folder.

2. Run main.py file.

3. Fill in the table as you need it and save it.

4. See the results in the next_month.txt file.

5. Copy the resulting table to the telegram_bot/files/tables folder under the name you need.

---

### Tips
- How to create new bot and get its token:

  - Write to @BotFather on telegram.

  - Type /newbot and and follow all the instructions.
    
  - Type /mybots and choose the your new bot.
    
  - Press API Token and copy it.

- How to get your chat's id:
  
  - Add @LeadConverterToolkitBot to your group.
 
  - Type /get_chat_id and copy it.
