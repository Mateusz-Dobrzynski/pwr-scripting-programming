import requests
from bs4 import BeautifulSoup
from lxml import etree

import re

from news_item import NewsItem


class WebScraper:
    def __init__(
        self,
        url: str,
        xpath: str,
        url_xpath,
        title_xpath: str,
        image_xpath: str = "",
    ) -> None:
        self.url = url
        self.xpath = xpath
        self.url_xpath = url_xpath
        self.title_xpath = title_xpath
        self.image_xpath = image_xpath
        pass

    def get_news_items(self) -> list[NewsItem]:
        news_items = []
        HEADERS = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5",
        }
        webpage = requests.get(self.url, headers=HEADERS)
        if webpage.status_code != 200:
            raise Exception("Error performing HTTP request")
        soup = BeautifulSoup(webpage.content, "html.parser")
        dom = etree.HTML(str(soup), parser=None)
        elements = dom.xpath(self.xpath)
        for i in range(len(elements)):
            news_items.append(
                NewsItem(dom, i, self.url_xpath, self.title_xpath, self.image_xpath)
            )
        return news_items

    def _remove_xa0_from(self, text: str) -> str:
        return text.replace("\xa0", " ")
