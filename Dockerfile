FROM python:3.7
RUN  apt-get update &&apt-get upgrade -y&& apt-get install python-pip -y
RUN pip install --upgrade pip
RUN pip install scrapy
WORKDIR scrapy_assigment
COPY . .
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV sites default
# ENTRYPOINT ["scrapy"]
# CMD ["crawl spider", "-a start_urls=$sites"]
CMD []