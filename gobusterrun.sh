#!/bin/bash
service tor start
echo "[+] The Url >> "
read url
echo $url > url.txt
gobuster dir -u $url -w /usr/share/wordlists/dirb/common.txt -o mrx.txt

python3 gobusterrun.py
