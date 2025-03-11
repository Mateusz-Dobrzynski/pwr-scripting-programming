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
        image_xpath: str = "",
    ):
        self.index = index
        self.url_xpath = url_xpath
        self.url = self._get_url_from(element)
        self.title_xpath = title_xpath
        self.title = self._get_title_from(element)
        if image_xpath != "":
            self.image_xpath = image_xpath
            self.image_url = self._get_image_url_from(element)

    def _get_url_from(self, element):
        return element.xpath(self.url_xpath)[self.index].get("href")

    def _get_image_url_from(self, element):
        return element.xpath(self.image_xpath)[self.index].get("src")

    def _get_title_from(self, element):
        return element.xpath(self.title_xpath)[self.index].text
