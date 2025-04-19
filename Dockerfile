FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
ENV CHROME_BIN=/usr/bin/google-chrome-stable
WORKDIR /app
RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    unzip \
    ca-certificates \
    fontconfig \
    libx11-dev \
    libxkbfile-dev \
    libnss3-dev \
    libxrender1 \
    libfontconfig1 \
    libdbus-1-3 \
    libxcomposite1 \
    libxdamage1 \
    libasound2 \
    libnspr4 \
    libgdk-pixbuf2.0-0 \
    libatk1.0-0 \
    libgtk-3-0 \
    libgbm1 \
    google-chrome-stable \
    && apt-get clean
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "animesh:app"]