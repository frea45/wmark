
import os
import ffmpeg
from pyrogram import Client, filters

api_id = 3335796
api_hash = "138b992a0e672e8346d8439c3f42ea78 "
bot_token = "7136875110:AAFzyr2i2FbRrmst1sklkJPN7Yz2rXJvSew"

app = Client("watermark_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("سلام! فقط ویدیو بفرست تا برات واترمارک بزنم.")


@app.on_message(filters.video & filters.private)
async def add_watermark(client, message):
    downloading = await message.reply("در حال دریافت ویدیو...")

    input_path = await message.download(file_name="input.mp4")
    output_path = "output.mp4"
    watermark_text = "hello world"

    try:
        # افزودن واترمارک با ffmpeg
        ffmpeg.input(input_path).output(
            output_path,
            vf=f"drawtext=text='{watermark_text}':fontcolor=white:fontsize=24:x=10:y=10",
            codec="libx264",
            acodec="aac",
            preset="ultrafast"
        ).run(overwrite_output=True)

        await downloading.edit("در حال ارسال فایل...")
        await message.reply_video(video=output_path, caption="ویدیو با واترمارک آماده‌ست!")

    except Exception as e:
        await downloading.edit(f"خطا در پردازش ویدیو: {e}")

    finally:
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)


app.run()
