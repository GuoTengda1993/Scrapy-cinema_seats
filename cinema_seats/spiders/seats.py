# -*- coding: utf-8 -*-
import scrapy
from ..items import CinemaSeatsItem
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeatsSpider(scrapy.Spider):
    name = 'seats'
    base_url = 'http://maoyan.com/xseats/20180211'
    start_urls = []
    for i in range(1,1000000):
        s = '%07d' % i
        url = base_url + str(s)
        start_urls.append(url)

    def parse(self, response):
        #判断是否被限制
        if response.css('head>title::text').extract_first() == '猫眼访问控制':

            driver = webdriver.PhantomJS()
            driver.get('http://maoyan.com/')

            captcha_url = driver.find_element_by_css_selector('div.row>img').get_attribute('src')
            resp = requests.get(captcha_url)
            img = Image.open(BytesIO(resp.content))
            img.show()
            captcha = input('请输入验证码：')

            element = driver.find_element_by_name('captcha_code')
            element.send_keys(captcha, Keys.ENTER)
            #driver.find_element_by_css_selector('button.row').click()
            driver.close()

        else: #计算厅座位数
            if response.css('div.modal p.tip::text').extract_first() == '场次信息不存在':
                yield None
            else:
                cinemas = CinemaSeatsItem()
                row = response.css('div.seats-wrapper>div.row')
                all_seats = []
                i = 0
                for seats in row:
                    seat1 = seats.css('span.seat.selectable::attr(data-column-id)').extract()
                    seat2 = seats.css('span.seat.sold::attr(data-column-id)').extract()
                    row_num = len(seat1 + seat2)
                    all_seats.append(int(row_num))
                cinemas['all_num'] = sum(all_seats)
                cinema = response.css('div.show-info>div.info-item:nth-child(1)>span.value.text-ellipsis::text').extract_first()
                room = response.css('div.show-info>div.info-item:nth-child(2)>span.value.text-ellipsis::text').extract_first()
                cinemas['cinema_name'] = cinema
                cinemas['room_num'] = room
                yield cinemas

