from flask import Flask, render_template, redirect, url_for
from telethon import TelegramClient, events
import threading
import time

app = Flask(__name__)

api_id = '29781864'
api_hash = 'cc05cf284195557866937e39bdb91cd7'
phone_number = '+963994232087'
channel_username = '@yyffghgguhfyjgyjhfghff6hg'

client = TelegramClient('session_name', api_id, api_hash)

async def start_bot():
    await client.start()

    @client.on(events.NewMessage(chats=channel_username))
    async def my_event_handler(event):
        print(f"New Message: {event.text}")
        # me = await client.get_me()  # الحصول على معلومات المستخدم
        # user_id = me.id  # الحصول على معرف المستخدم
        await client.send_message("me" , event.text)

    await client.run_until_disconnected()

def run_bot():
    import asyncio
    asyncio.run(start_bot())

bot_thread_bot = threading.Thread(target=run_bot)

@app.route('/')
def index():
    if bot_thread_bot.is_alive():
        running = True
    else:
        running = False
    return render_template('index.html',  running=running)



@app.route('/start-bot')
def start_bot_route():
    bot_thread_bot = westart(bot_thread_bot, run_bot)
    return redirect(url_for('index'))

def westart(fish, fun):
    if fish.is_alive():
        time.sleep(1)
        return fish
    else:
        time.sleep(10)
        try:
            fish.start()
            print(f"{fish}  ::  The Bot started successfully.")
            return fish
        except RuntimeError:
            fish = threading.Thread(target=fun)
            fish.start()
            print(f"{fish}  ::  Bot restarted successfully.")
            return fish

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
