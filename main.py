import revolt
import asyncio
import os

TOKEN = os.getenv("TOKEN")

class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        matcher = {
            "www.instagram.com": "d.ddinstagram.com",
            "/instagram.com": "/d.ddinstagram.com",
            "www.twitter.com" : "d.fxtwitter.com",
            "/twitter.com": "/d.fxtwitter.com",
            "www.x.com": "d.fixupx.com",
            "/x.com": "/d.fixupx.com",
            "www.reddit.com": "www.vxreddit.com",
            "/reddit.com": "/vxreddit.com"
        }
        for url in matcher:
            if url in message.content:
                resp = message.content.replace(url, matcher[url])
                await message.channel.send(resp)

async def main():
    async with revolt.utils.client_session() as session:
        client = Client(session, TOKEN)
        await client.start()

asyncio.run(main())