FROM python:3.10-slim

RUN apt update &&     apt install -y ffmpeg git &&     apt clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]
