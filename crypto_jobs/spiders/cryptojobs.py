import scrapy


class CryptojobsSpider(scrapy.Spider):
    name = 'cryptojobs'
    allowed_domains = ['crypto.jobs']
    start_urls = ['https://crypto.jobs/']

    def parse(self, response):
        print(response)
        print(1)
