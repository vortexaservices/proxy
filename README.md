I don't own the TCP proxy file but I coded the shitty auto screener

Commands:
apt install screen python3 -y
screen -dmS auto python3 auto.py
chmod +x *
screen -dmS ServerIPAddress ./tcp-proxy -l :ProxyPort-r ServerIPAddress:CNCPort
