# linkfix-oss-revolt
A bot that fixes embed links on [Revolt](https://revolt.chat) to serve media links.

## Working
This bot fixes media embed links of the following websites:
Twitter/X - via [fxtwitter](https://github.com/FixTweet/FixTweet)
Instagram - via [ddinstagram](https://github.com/Wikidepia/InstaFix)
Reddit - via [vxreddit](https://github.com/dylanpdx/vxReddit)

It is in essence, a simple script that replaces domain names in order to fix links to display media on Revolt.

## Running
````
git clone https://github.com/afk-echo/linkfix-oss-revolt.git
cd linkfix-oss-revolt
python -m venv .venv
source .venv/bin/activate
pip install revolt
python main.py
````
