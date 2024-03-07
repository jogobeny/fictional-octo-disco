FROM python:3.11.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
WORKDIR /app/sreality_scrapper
CMD ["scrapy", "crawl", "sreality", "--loglevel", "INFO"]
