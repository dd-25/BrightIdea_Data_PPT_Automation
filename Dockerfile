# Use official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies required by Chrome and Selenium
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
    libgbm1 \
    xdg-utils \
    && apt-get clean

# Install Google Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \
    apt-get -y -f install && \
    rm google-chrome-stable_current_amd64.deb

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    rm chromedriver_linux64.zip

# Copy the current directory contents into the container at /app
COPY . /app/

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for the Flask app
EXPOSE 5000

# Set environment variable for the Chrome binary location
ENV CHROME_BIN="/usr/bin/google-chrome-stable"

# Run the Flask application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "animesh:app"]