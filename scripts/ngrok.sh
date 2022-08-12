##!/bin/sh
#echo "pwd of ngrok.sh"
#echo $PWD;ls -l
## Set local port from command line arg or default to 8080
#LOCAL_PORT=8000
#
#echo "Start ngrok in background on port [ $LOCAL_PORT ]"
#nohup ngrok http ${LOCAL_PORT} &>/dev/null &
#
#echo -n "Extracting ngrok public url ."
##my_ip=getent hosts $(cat /etc/hostname) | awk '{print $1; exit}'
##echo $my_ip
##NGROK_PUBLIC_URL=""
##while [ -z "$NGROK_PUBLIC_URL" ]; do
##  # Run 'curl' against ngrok API and extract public (using 'sed' command)
##  export NGROK_PUBLIC_URL=$(curl http://localhost:4040/api/tunnels)
##  sleep 1
##  echo -n "."
##done
##
##echo
#python scripts/extract_url.py > url.txt
#
#value=`cat scripts/url.txt`
#echo "$value"
#sleep 10
#echo "NGROK_PUBLIC_URL => [ $value ]"
#
#yum install -y npm
#yum install -y nodejs
#
#echo npm -v
#
#npm install -g twilio-cli
#
#export TWILIO_ACCOUNT_SID=AC9c97bcd2de84f7993a7a0f55780674a4
#export TWILIO_AUTH_TOKEN=a0d8e0562c48f4ed884f82100fbcb8c7
#twilio api:core:incoming-phone-numbers:update \
#    --sid PNfc7c07aea2ec823e6b6cff8d7ffb6d0c \
#    --voice-url $value"/shipping_ivr/welcome"

#!/bin/sh

# Set local port from command line arg or default to 8080
LOCAL_PORT=8000

echo "Start ngrok in background on port [ $LOCAL_PORT ]"
nohup ngrok http ${LOCAL_PORT} &>/dev/null &

echo -n "Extracting ngrok public url ."
NGROK_PUBLIC_URL=""
while [ -z "$NGROK_PUBLIC_URL" ]; do
  # Run 'curl' against ngrok API and extract public (using 'sed' command)
  export NGROK_PUBLIC_URL=$(curl --silent --max-time 10 --connect-timeout 5 \
                            --show-error http://127.0.0.1:4040/api/tunnels | \
                            sed -nE 's/.*public_url":"https:..([^"]*).*/\1/p')
  sleep 1
  echo -n "."
done

echo
echo "NGROK_PUBLIC_URL => [ $NGROK_PUBLIC_URL ]"

apt-get install -y npm
apt-get install -y nodejs

echo npm -v

npm install -g --unsafe-perm=true --allow-root twilio-cli

export TWILIO_ACCOUNT_SID=AC9c97bcd2de84f7993a7a0f55780674a4
export TWILIO_AUTH_TOKEN=a0d8e0562c48f4ed884f82100fbcb8c7
twilio api:core:incoming-phone-numbers:update \
    --sid PNfc7c07aea2ec823e6b6cff8d7ffb6d0c \
    --voice-url "http://"$NGROK_PUBLIC_URL"/shipping_ivr/welcome"

