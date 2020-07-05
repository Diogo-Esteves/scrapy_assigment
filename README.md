Technical Assignment

How to run
* with docker container:
- docker build -t <name_of_image> .
~ docker container run -i <name_of_image> scrapy crawl spider -a start_urls=<sites_url>
- with more than one url:
~ docker container run -i <name_of_image> scrapy crawl spider -a start_urls=<sites_url1,sites_url2>

* with terminal:
- with the environment and requirements installed run ->
~ scrapy crawl spider -a start_urls=<sites_url>
- with more than one url:
~ scrapy crawl spider -a start_urls=<sites_url1, sites_url2>

-- in both to save in a json:
 ~ comand -o scrapy_site.json

Tecnical Overview

I chose to start the assignment with a structure of a project that can grows and be integrated if it wants.
Scrapy framework can give this to us, a structured project and not just a script.
I use scrapy concurrent variable set in settings to use concurrent tasks.