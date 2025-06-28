import scrapy


class LeverSpider(scrapy.Spider):
    name = "lever"
    allowed_domains = ["lever.com"]
    start_urls = [
        "https://jobs.lever.co/aventon/",
        "https://jobs.lever.co/Complex/",
        "https://jobs.lever.co/malbongolf/",
        "https://jobs.lever.co/brooksrunning/",
        "https://jobs.lever.co/arcteryx.com/"
    ]

    def parse(self, response):
        company_name = response.url.strip("/").split("/")[-1]
        groups = response.xpath('//div[@class="postings-group"]')
        for group in groups:
            group_title = group.css('.posting-category-title::text').get()
            positions = group.css('.posting')
            for position in positions:
                yield {
                    'company': company_name,
                    'group_title': group_title,
                    'position': position.css('.posting-title h5::text').get(),
                    'workplace': position.css('.workplaceTypes ::text').get().replace('\xa0—\xa0', ''),
                    'commitment': position.css('.commitment ::text').get(),
                    'location': position.css('.location ::text').get(),
                    'position_url': position.css('.posting-apply a::attr(href)').get(),
                }
