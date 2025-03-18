from news_item import NewsItem


class MarkdownGenerator:
    def __init__(self, news_items: list[NewsItem]) -> None:
        self.news_items: list[NewsItem] = news_items

    def save_to(self, path):
        text_content = "# News!\n\n"
        for item in self.news_items:
            text_content += f"## [{item.title}]({item.url})\n"
            if item.image_url:
                text_content += f'<img src="{item.image_url}">'
            text_content += "\n\n"
        file = open(path, "w")
        file.write(text_content)
        file.close()
