import os
import json

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUPS_ID = json.loads(os.getenv("GROUPS_ID"))
NOTIFY_HOUR = int(os.getenv("NOTIFY_HOUR"))
NOTIFY_MINUTE = int(os.getenv("NOTIFY_MINUTE"))