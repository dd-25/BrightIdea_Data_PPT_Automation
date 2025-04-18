# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV CHROME_BIN=/usr/bin/google-chrome-stable  # Default location for Linux-based systems

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
    libgdk-pixbuf2.0-0 \
    libatk1.0-0 \
    libgtk-3-0 \
    libgbm1 \
    google-chrome-stable \
    && apt-get clean

# Install Python dependencies (use the requirements.txt file)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port for the Flask app
EXPOSE 5000

# Set the command to run the Flask app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "animesh:app"]