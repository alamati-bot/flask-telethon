from flask import Flask, render_template, redirect, url_for
from telethon import TelegramClient, events
import threading

app = Flask(__name__)

api_id = '29781864'
api_hash = 'cc05cf284195557866937e39bdb91cd7'
phone_number = '+963994232087'
channel_username = '@yyffghgguhfyjgyjhfghff6hg'

client = TelegramClient('session_name', api_id, api_hash)

# دالة لتشغيل البوت
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-bot')
def start_bot_route():
    threading.Thread(target=run_bot).start()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
