#!/bin/bash
echo "Setting up Saba Null Framework..."
apt-get update
apt-get install -y python3 python3-pip openssl
pip3 install -r requirements.txt
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -subj "/C=US/CN=localhost"
chmod +x main_orchestrator.py
echo "Setup complete! Run: python3 main_orchestrator.py"
