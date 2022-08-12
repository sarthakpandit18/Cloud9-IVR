#!/bin/bash
echo "Starting script"
echo "pwd of main.sh"
echo $PWD;ls -l
#pip3 install --no-cache-dir -r /requirements.txt
#pip3 install requests
#curl -sL https://deb.nodesource.com/setup_12.x | bash -
#yum install -y nodejs
chmod 777 scripts
chmod 777 scripts/ngrok.sh
chmod 777 scripts/start.sh
sh scripts/ngrok.sh
sleep 10s
echo "Starting IVR application"
sh scripts/start.sh
