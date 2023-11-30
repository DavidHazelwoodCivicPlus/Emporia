import scrapy


class PeopleSpider(scrapy.Spider):
    name = "people"
    allowed_domains = ["www.town.dennis.ma.us"]
    start_urls = ["https://www.town.dennis.ma.us/departments"]

    def parse(self, response):
        pass
