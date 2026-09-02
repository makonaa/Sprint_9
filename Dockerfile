FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y chromium
RUN apt-get install -y chromium-driver

RUN which chromedriver
COPY . .

CMD ["pytest", "--alluredir", "allure-results"]