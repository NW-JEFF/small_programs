import scrapy, re, sys, os
a=os.path.dirname(os.path.dirname(__file__))
sys.path.append(a)
from items import HornydragonItem


class DownloadpicsSpider(scrapy.Spider):
    name = 'downloadpics'
    start_urls = ['http://hornydragon.blogspot.com/']

    def parse(self, response):
        #pat=re.compile(r'雜七雜八短篇漫畫翻譯\d{4}')
        np={"re": "http://exslt.org/regular-expressions"}
        self.count = 0
        for href in response.xpath(r'//a[re:match(@title, "雜七雜八短篇漫畫翻譯\d{4}")]/@href',namespaces=np).extract():
            try:
                yield scrapy.Request(href, callback=self.parse_web)
            except:
                continue


    def parse_web(self, response):
        for pic in response.css('img[src$="jpg"]::attr(src)').extract():
            item=HornydragonItem()
            self.count+=1
            item['img_name']=str(self.count)+pic.split('/')[-1]
            item['img_src']=pic
            yield item


