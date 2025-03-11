from liczyrzepa.web_scraper import WebScraper


class TestWebScraper:
    def test_url_scraping(self):
        # GIVEN
        page_url = (
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/"
        )
        main_xpath = "//div[contains(@id,'post')]"
        url_xpath = "//div[contains(@id, 'post')]//div[@class='title']/h2/a"
        expected_urls = [
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/uruchamiamy-2-dniowe-praktyczne-szkolenie-z-osint-u/",
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/tajemnice-bankowe-i-inne-wrazliwe-dane-polakow-lataja-po-docer-pl/",
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/ponad-260-tys-kary-za-to-ze-iod-byl-podwladnym-szefa-dzialu-bezpieczenstwa/",
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/atak-ransomware-na-eurocert-wyciekly-nawet-wizerunki-klientow/",
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/cyberbezpieczenstwo-duze-banki/",
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/znow-probuja-przepchnac-cenzure-w-internecie-czyli-o-ciekawej-wrzutce-ministerstwa-cyfryzacji-w-propozycje-ustawy-o-e-uslugach/",
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/uwaga-ktos-podszywa-sie-pod-krajowa-administracje-skarbowa/",
        ]

        # WHEN
        news_items = WebScraper(
            page_url, main_xpath, url_xpath, title_xpath=url_xpath
        ).get_news_items()

        # THEN
        for i in range(len(expected_urls)):
            assert news_items[i].url == expected_urls[i]

    def test_image_scraping(self):
        # GIVEN
        page_url = (
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/"
        )
        main_xpath = "//div[contains(@id,'post')]"
        url_xpath = "//div[contains(@id, 'post')]//div[@class='title']/h2/a"
        image_xpath = (
            "//div[contains(@id, 'post')]//img[contains(@class, 'wp-post-image')]"
        )
        expected_urls = [
            "https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/01/szkolenie-osint-2-dni-150x150.jpg",
            "https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2025/02/listy-oper-wyszuk-600x292.png",
        ]

        # WHEN
        news_items = WebScraper(
            page_url,
            main_xpath,
            url_xpath,
            title_xpath=url_xpath,
            image_xpath=image_xpath,
        ).get_news_items()

        # THEN
        for i in range(len(expected_urls)):
            assert news_items[i].image_url == expected_urls[i]

    def test_title_scraping(self):
        # GIVEN
        page_url = (
            "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/"
        )
        main_xpath = "//div[contains(@id,'post')]"
        url_xpath = "//div[contains(@id, 'post')]//div[@class='title']/h2/a"
        image_xpath = (
            "//div[contains(@id, 'post')]//img[contains(@class, 'wp-post-image')]"
        )
        expected_titles = [
            "Uruchamiamy 2 dniowe, praktyczne szkolenie z OSINT-u!",
            "Tajemnice bankowe i inne wrażliwe dane Polaków latają po Docer.pl",
            "Ponad 260 tys. kary za to, że IOD był podwładnym szefa działu bezpieczeństwa",
            "Atak ransomware na EuroCert. Wyciekły nawet wizerunki klientów",
            "Jak wygląda cyberbezpieczeństwo w dużym banku? I jak takie banki reagują na ataki?",
        ]

        # WHEN
        news_items = WebScraper(
            page_url,
            main_xpath,
            url_xpath,
            title_xpath=url_xpath,
            image_xpath=image_xpath,
        ).get_news_items()

        # THEN
        for i in range(len(expected_titles)):
            assert news_items[i].title == expected_titles[i]
