## Duty notifier

### Warning
Works with the sample table at the path files/attendants_teable.txt

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
apt install -y python3.13
curl -sSL https://bootstrap.pypa.io/get-pip.py | python3.13
apt install python3.13-venv
python3.13 -m venv venv
source venv/bin/activate
pip3.13 install -r requirements.txt
deactivate
```

3. Put your bot token and chat's id to files/credentials.py

4. Run deploy script: `bash deploy.sh`

5. Giving the bot access to messages
    - Type /mybots in chat with @BotFather and select a bot

    - Press "Bot Settings" --> "Group Privacy"

    - Press "Turn off"
  
6. Adding a list of commands
    - Type /setcommands in chat with @BotFather and select a bot
  
    - Type the following:
      ```
      current_attendant - {description} # This command will show you the current duty officer and his deputy
      week_attendants - {description} # This command will show you the duty officers and their deputies for the current week
      ```

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
