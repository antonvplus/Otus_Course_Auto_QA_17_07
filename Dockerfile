FROM python:3.14-slim

WORKDIR /app

RUN apt-get update && apt-get install -y\
                        chromium \
                        firefox-esr \
                        curl \
                        libatk-bridge2.0-0 \
                        libgtk-3-0 \
                        libgbm1 \
                        libasound2


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["pytest", "--OS", "linux"]
CMD ["tests/"]