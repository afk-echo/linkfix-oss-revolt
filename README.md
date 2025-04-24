# linkfix-oss-revolt
A bot that fixes embed links on [Revolt](https://revolt.chat) to serve media links.

## Working
This bot fixes media embed links of the following websites:

Twitter/X - via [fxtwitter](https://github.com/FixTweet/FixTweet)

Instagram - via [ddinstagram](https://github.com/Wikidepia/InstaFix)

Reddit - via [vxreddit](https://github.com/dylanpdx/vxReddit)

It is in essence, a simple script that replaces domain names in order to fix links to display media on Revolt.

## Running
### Create a bot
Create a Revolt bot on the desktop app by going to `User Settings > My Bots > Create a Bot`. Give it a name and copy the token of the bot. Add this bot to a group/server for it to work in. Replace `"enter your token"` in the following steps with the token of this bot. 

### Linux
Use a shell of your choice and do the following:
1. Clone the repository and install dependencies:
````
git clone https://github.com/afk-echo/linkfix-oss-revolt.git
cd linkfix-oss-revolt
python -m venv .venv
source .venv/bin/activate
pip install revolt.py
````
2. Activate the environment and run main.py:
````
source .venv/bin/activate
TOKEN="enter your token" python main.py
````

### Windows (untested)
Start a PowerShell session and do the following:
1. Clone the repository and install dependencies:
````
git clone https://github.com/afk-echo/linkfix-oss-revolt.git
cd linkfix-oss-revolt
python -m venv .venv
source .venv/scripts/Activate.ps1
pip install revolt.py
````
2. Activate the environment and run `main.py`:
````
source .venv/scripts/Activate.ps1
$env:TOKEN = "enter your token"
python main.py
````

## Issues
When installing `revolt.py` using `pip`, you may face issues installing `aiohttp` if you are on a newer version of Python (this issue is known to occur on Python 3.13.3 and above). To mitigate this issue, you may choose to clone the [revolt.py](https://github.com/revoltchat/revolt.py/tree/master) repository yourself and install `revolt.py` from source manually. To do this, run the following:

````
git clone https://github.com/revoltchat/revolt.py.git
cd revolt.py
pip install .
````

You can now try to activate the environment and run main.py as per the instructions for your particular operating system.
