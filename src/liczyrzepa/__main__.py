import argparse
from chart_creator import ChartCreator
from gui import GUI
from markdown_generator import MarkdownGenerator
from spreadsheet_saver import SpreadsheetSaver
from price_history import PriceHistory
from web_scraper import WebScraper


def main():
    parser = construct_argument_parser()
    args = parser.parse_args()


def construct_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to save output to")
    parser.add_argument("--url", help="The URL of a website you want to monitor")
    parser.add_argument("--url-xpath", help="URL Xpath")
    parser.add_argument("-x", "--xpath", help="The XPath leading to a news item")
    parser.add_argument("-t", "--title", help="Title xpath")
    parser.add_argument("-i", "--image", help="Image xpath")
    return parser


if __name__ == "__main__":
    main()
    parser = construct_argument_parser()
    args = parser.parse_args()
    main_xpath = args.xpath
    if not main_xpath:
        raise Exception("Please define Xpath leading to news items")
    url_xpath = args.url_xpath
    if not url_xpath:
        raise Exception("Please define a general Xpath leading to article URLs")
    url = args.url
    if not url:
        raise Exception("Please define target URL")
    title = args.title
    if not title:
        raise Exception("Please define title XPath")
    image = args.image
    file = args.file
    if not file:
        raise Exception("Please define output directory")
    scraper = WebScraper(url, main_xpath, url_xpath, title, image)
    news_items = scraper.get_news_items()
    MarkdownGenerator(news_items).save_to(file)
