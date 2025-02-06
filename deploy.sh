#!/usr/bin/env bash

cat <<EOF > /etc/systemd/system/duty_notifier.service

[Unit]
Description=Telegram duty notifier
After=network.target

[Service]
WorkingDirectory=/opt/duty-notifier
ExecStart=/opt/duty-notifier/venv/bin/python3.13 /opt/duty-notifier/main.py
ExecReload=/opt/duty-notifier/venv/bin/python3.13 /opt/duty-notifier/main.py
ExecRestart=/opt/duty-notifier/venv/bin/python3.13 /opt/duty-notifier/main.py

[Install]
WantedBy=multi-user.target
EOF

systemctl enable --now duty_notifier
