# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class HornydragonPipeline(ImagesPipeline):
    # 对图片数据进行请求发送
    # 该方法参数item就是接受爬虫文件提交过来的item
    def get_media_requests(self, item, info):
        # meta可以将字典传递给file_path方法
        yield scrapy.Request(item['img_src'], meta={'item': item})

    # 指定图片存储的路径
    def file_path(self, request, response=None, info=None):
        # 如何获取图片名称
        item = request.meta['item']
        img_name = item['img_name']
        return img_name

    # 可以将item 传递给下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item
