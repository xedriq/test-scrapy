import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksPriceSpider(CrawlSpider):
    name = 'books_price'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]')),
    )

    def parse_item(self, response):
        yield {
            'title' : response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get(),
            'price' : response.xpath('//p[@class="price_color"]/text()').get()
        }
