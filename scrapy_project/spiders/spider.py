# -*- coding: utf-8 -*-
import scrapy, re
from scrapy import Request
from ..items import Scrapy_projectItem


class SpiderSpider(scrapy.Spider):
    name = "spider"

    def __init__(self, **args):
        self.start_urls = args.get("start_urls").split(",")

    def start_requests(self):
        start_urls = reversed(self.start_urls)
        return [Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        if response.status == 404:
            print("DeadPage")
        else:
            site = Scrapy_projectItem()

            site["logo"] = str(response.css("img::attr(src)").extract_first())
            site["phones"] = self.get_phones(response.text)
            site["website"] = str(response.url)

            print(site)
            yield site

    def get_phones(self, phones):
        return (
            re.findall(r"\+\d{2}\s?0?\d{9}", phones)
            + re.findall(r"\+\d{3}\s?0?\d{3}\s?0?\d{3}", phones)
            + re.findall(r"\d{3}\s?0?\d{3}\s?0?\d{3}", phones)
            + re.findall(r"\d{2}\s?0?\d{2}\s?0?\d{2}", phones)
        )
