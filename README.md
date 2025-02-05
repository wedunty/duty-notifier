## Duty notifier

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
apt update
apt install python3.13
curl -sSL https://bootstrap.pypa.io/get-pip.py | python3.13
apt install python3.13-venv
python3.13 -m venv myenv
source myenv/bin/activate
pip3.13 install -r requirements.txt
```

3. Put your bot token and chat's id to files/credentials.py

4. Run deploy script: `bash deploy.sh`

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
