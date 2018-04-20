# -*- coding: utf-8 -*-
import scrapy

# 直接用cookies提交
class RenrenScrapySpider(scrapy.Spider):
    name = 'renren_scrapy'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']
    cookies = {
        '_de': '79C41491BD26430A5DE0DF1A730F8DFE',
        '_r01_': '1',
        'anonymid': 'jfqsml2a-q75bu1',
        'ch_id': '10016',
        'depovince': 'GW',
        'first_login_flag': '1',
        'ick_login': 'aedf3a7d-4faf-4a14-bec5-a2407b0d46ac',
        'id': '824673911',
        'jebe_key': '75fb1888-637d-445e-a62e-0c10bf530328%7C41cdfdffe03854fea4a9a1b782a42fb7%7C1523191155591%7C1%7C1523191156327',
        'jebecookies': 'c1a14341-1085-4e38-89de-2e22a37eec7c|||||',
        'ln_hurl': 'http://head.xiaonei.com/photos/0/0/men_main.gif',
        'ln_uact': '32336434@qq.com',
        'loginfrom': 'syshome',
        'p': '82f1cf894ea7730591d8b239bc05a32c1',
        'societyguester': '51842541df599b50f94356096709bc601',
        't': '51842541df599b50f94356096709bc601',
        'xnsid': '5abb7f0f',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        print(response)
