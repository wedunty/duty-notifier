## Duty notifier

### Requirements
- git
- docker

### Warning
Works with the sample table at the path files/1'st_table.txt without empty lines

### Installation
1. Download to /opt folder: 

    ```
    cd /opt
    git clone https://github.com/wedunty/duty-notifier.git
    cd duty-notifier/
    ```

2. Configuring the bot:
    - Open .env file.

    - Put your bot's token, group(s) id and timezone like this:
      ```
      BOT_TOKEN=0123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
      GROUPS_ID={"1'st": "xxxxxxxxxxxx", "2'nd": "xxxxxxxxxxxx", "3'rd": "xxxxxxxxxxxx", "4'th": "xxxxxxxxxxxx"}
      TZ=your_continent/your_city
      ```
    - Open files/tables.

    - Add as many tables as you need (in the same format as the sample table).

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
    - Go to project directory: `cd /opt/duty-notifier`
    - Create an image: `docker build -t {name of your image} .`
    - Start the image: `docker run --env-file .env -v ./files/tables:/duty-notifier/files/tables --name {name of your container} {name of your image}`

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
