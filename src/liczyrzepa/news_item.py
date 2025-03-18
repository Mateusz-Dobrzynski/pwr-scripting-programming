class NewsItem:
    url: str
    image_url: str
    title: str

    def __init__(
        self,
        element,
        index: int,
        url_xpath: str,
        title_xpath: str,
        image_xpath: str | None = None,
    ):
        self.index = index
        self.url_xpath = url_xpath
        self.title_xpath = title_xpath
        if element != None:
            if url_xpath != None:
                self.url = self._get_url_from(element)
            if title_xpath != None:
                self.title = self._get_title_from(element)
        if image_xpath:
            self.image_xpath = image_xpath
            self.image_url = self._get_image_url_from(element)
        else:
            self.image_url = None

    def _get_url_from(self, element):
        return element.xpath(self.url_xpath)[self.index].get("href")

    def _get_image_url_from(self, element):
        return element.xpath(self.image_xpath)[self.index].get("src")

    def _get_title_from(self, element):
        return element.xpath(self.title_xpath)[self.index].text
