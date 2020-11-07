docker build -t lookscrape . &&
docker run --name lookscrape -v $(pwd):/app lookscrape