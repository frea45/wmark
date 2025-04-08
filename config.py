import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN","7136875110:AAFzyr2i2FbRrmst1sklkJPN7Yz2rXJvSew")
	API_ID = int(os.environ.get("API_ID",3335796))
	API_HASH = os.environ.get("API_HASH","138b992a0e672e8346d8439c3f42ea78")
