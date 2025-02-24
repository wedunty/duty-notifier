## Duty notifier

### Warning
Works with the sample table at the path files/attendants_teable.txt without empty lines

### Installation
1. Download to /opt folder: 

```
cd /opt
git clone https://github.com/wedunty/duty-notifier.git
cd duty-notifier/
```

2. Install python3.13, create virtual environment and install requirements for the bot:

```
add-apt-repository ppa:deadsnakes/ppa
apt -y update
apt install -y python3.13 python3.13-venv
curl -sSL https://bootstrap.pypa.io/get-pip.py | python3.13
python3.13 -m venv venv
source venv/bin/activate
pip3.13 install -r requirements.txt
deactivate
```

3. Configuring the bot
    - Open files/credentials.py
    - Put your bot's token and group/groups id like this:
      ```
      BOT_TOKEN = "0123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      GROUPS_ID = {"1'st": "xxxxxxxxxxxx",
                   "2'nd": "xxxxxxxxxxxx",
                   "3'rd": "xxxxxxxxxxxx",
                   "4'th": "xxxxxxxxxxxx"
                   }
      ```
    - Open files/tables
    - Add as many tables as you need (in the same format as the sample table).
    - Each table must begin with what you have specified as the key to the group ID for which the table is intended

4. Giving the bot access to messages
    - Type /mybots in chat with @BotFather and select a bot

    - Press "Bot Settings" --> "Group Privacy"

    - Press "Turn off"
  
5. Adding a list of commands
    - Type /setcommands in chat with @BotFather and select a bot
  
    - Type the following:
      ```
      current_attendant - {description} # This command will show you the current duty officer and his deputy
      week_attendants - {description} # This command will show you the duty officers and their deputies for the current week
      ```
      
6. Run deploy script: `bash deploy.sh`

---

### Tips
- How to create new bot and get its token:

  - Write to @BotFather on telegram

  - Type /newbot and and follow all the instructions
    
  - Type /mybots and choose the your new bot
    
  - Press API Token and copy it

- How to get your chat's id:
  
  - Add @LeadConverterToolkitBot to your group
 
  - Type /get_chat_id and copy it
