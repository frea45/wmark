from pyrogram import Client, filters
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

API_ID = 123456  # جایگزین کن با API ID خودت
API_HASH = "your_api_hash"  # جایگزین کن با API HASH خودت
BOT_TOKEN = "your_bot_token"  # جایگزین کن با توکن ربات

app = Client("watermark_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video)
async def watermark(client, message):
    msg = await message.reply("در حال پردازش ویدیو...")

    file_path = await message.download()
    output_path = "output.mp4"

    clip = VideoFileClip(file_path)
    txt = TextClip("hello world", fontsize=24, color='white').set_pos(("left", "top")).set_duration(clip.duration)
    final = CompositeVideoClip([clip, txt])
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")

    await message.reply_video(output_path)
    await msg.delete()
    os.remove(file_path)
    os.remove(output_path)

app.run()
