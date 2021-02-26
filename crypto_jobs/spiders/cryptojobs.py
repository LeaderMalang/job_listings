import scrapy
import w3lib.html

class CryptojobsSpider(scrapy.Spider):
    name = 'cryptojobs'
    allowed_domains = ['crypto.jobs']
    start_urls = ['https://crypto.jobs/']

    def parse(self, response):

        jobs=response.css('.table-jobs').xpath('//tbody/tr[@class="highlighted"]')
        for job in jobs:
            # print(job)
            # company_ico=job.css('img::attr(src)').get()
            job_url=job.css('.job-url::attr(href)').get()
            # company_name=job.css('.job-url span::text').get()
            # job_type_container=job.css('.hidden-xs').xpath('//small/span[1]').get()
            # job_type = w3lib.html.remove_tags(job_type_container)
            # job_industry_container = job.css('.hidden-xs').xpath('//small/span[2]').get()
            # job_industry = w3lib.html.remove_tags(job_type_container)
            url = response.urljoin(job_url)
            if url:
                yield scrapy.Request(url=url, callback=self.single_parse)

        nextUrl=response.css('ul.pagination li:last-of-type a::attr(href)').get()
        if nextUrl:
            nextPageUrl=response.urljoin(nextUrl)
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
            yield scrapy.Request(url=nextPageUrl, callback=self.parse,
                                 headers=headers,
                                 method='GET')



    def single_parse(self,response):
        items=dict()
        print(response)