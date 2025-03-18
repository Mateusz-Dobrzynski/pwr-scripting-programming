from markdown_generator import MarkdownGenerator
from web_scraper import WebScraper
from os import getcwd


class TestMarkdownGenerator:
    def saved_file_should_have_proper_content():
        # GIVEN
        url = "https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/"
        main_xpath = "//div[contains(@id,'post')]"
        url_xpath = "//div[contains(@id, 'post')]//div[@class='title']/h2/a"
        title_xpath = url_xpath
        image_xpath = (
            "//div[contains(@id, 'post')]//img[contains(@class, 'wp-post-image')]"
        )
        output_path = f"{getcwd()}/test_output_file.md"

        # WHEN
        scraper = WebScraper(
            url,
            main_xpath,
            url_xpath,
            title_xpath,
            image_xpath,
        )
        items = scraper.get_news_items()
        MarkdownGenerator(items).save_to(output_path)

        # THEN
        file = open(output_path)
        content = file.read()
        assert (
            content
            == """
# News!

## [Uruchamiamy 2 dniowe, praktyczne szkolenie z OSINT-u!](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/uruchamiamy-2-dniowe-praktyczne-szkolenie-z-osint-u/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/01/szkolenie-osint-2-dni-150x150.jpg">

## [Tajemnice bankowe i inne wrażliwe dane Polaków latają po Docer.pl](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/tajemnice-bankowe-i-inne-wrazliwe-dane-polakow-lataja-po-docer-pl/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2025/02/listy-oper-wyszuk-600x292.png">

## [Ponad 260 tys. kary za to, że IOD był podwładnym szefa działu bezpieczeństwa](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/ponad-260-tys-kary-za-to-ze-iod-byl-podwladnym-szefa-dzialu-bezpieczenstwa/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2025/01/9heqew-150x150.jpg">

## [Atak ransomware na EuroCert. Wyciekły nawet wizerunki klientów](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/atak-ransomware-na-eurocert-wyciekly-nawet-wizerunki-klientow/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2025/01/swl-euroc-150x150.png">

## [Jak wygląda cyberbezpieczeństwo w dużym banku? I jak takie banki reagują na ataki?](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/cyberbezpieczenstwo-duze-banki/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2025/01/hsbc-title2-150x150.jpg">

## [Znów próbują przepchnąć cenzurę w internecie? Czyli o ciekawej wrzutce Ministerstwa Cyfryzacji w propozycję ustawy o e-usługach](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/znow-probuja-przepchnac-cenzure-w-internecie-czyli-o-ciekawej-wrzutce-ministerstwa-cyfryzacji-w-propozycje-ustawy-o-e-uslugach/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2025/01/RCL-150x150.png">

## [⚠️ Uwaga! Ktoś podszywa się pod Krajową Administrację Skarbową](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/uwaga-ktos-podszywa-sie-pod-krajowa-administracje-skarbowa/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2025/01/KAS-scam-150x150.jpg">

## [Jak zarządzać smartfonami pracowników i domowników? Czyli o stosowaniu systemów MDM słów kilka.](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/jak-zarzadzac-smartfonami-pracownikow-i-domownikow-czyli-o-stosowaniu-systemow-mdm-slow-kilka/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2021/06/podcast-logo-jpg.001-150x150.jpeg">

## [1,5 mln kary za niedopilnowanie modernizacji strony](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/15-mln-kary-za-niedopilnowanie-modernizacji-strony/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/12/OIG1.f2f1FONx60bmq3te7u8v-150x150.jpg">

## [Dlaczego warto kupić vouchery Niebezpiecznika na 2025?](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/dlaczego-warto-kupic-vouchery-niebezpiecznika-na-2025/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2022/11/sdr-szkolenie-150x150.jpg">

## [Zagrożenia zdalnego dostępu do komputera](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/zagrozenia-zdalnego-dostepu-do-komputera/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2021/06/podcast-logo-jpg.001-150x150.jpeg">

## [Poważna wpadka Netfliksa w Polsce. Dane kilku tysięcy Polaków wyciekły](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/powazna-wpadka-netfliksa-w-polsce-dane-kilku-tysiecy-polakow-wyciekly/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/12/netflix-hacked-150x150.jpg">

## [Poznaj tajemnice pracy detektywa i dowiedz się jak zakładać i wykrywać podsłuchy!](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/tajemnice-pracy-detektywa/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/12/detektyw-wide-150x150.jpg">

## [Czy polskie firmy są bezpieczniejsze od FC Barcelony? Cyberportret autorstwa ESET sugeruje, że nie do końca](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/czy-polskie-firmy-sa-bezpieczniejsze-od-fc-barcelony-cyberportret-autorstwa-eset-sugeruje-ze-nie-do-konca/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/10/higiena-150x150.png">

## [⚠️ Ruszył atak na klientów banku Santander](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/ruszyl-atak-na-klientow-banku-santander/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/11/cyberalert-santader-150x150.jpg">

## [Kulisy obsługi incydentów w polskich firmach](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/jak-poprawnie-obslugiwac-incydenty/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/10/incydent2-150x150.jpg">

## [Nowoczesne firewalle z AI, analiza szyfrowanego ruchu i Hypershield](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/nowoczesne-firewalle-z-ai-analiza-szyfrowanego-ruchu-i-hypershield/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2021/06/podcast-logo-jpg.001-150x150.jpeg">

## [⚠️ Uwaga na e-maile o naruszeniu praw autorskich](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/uwaga-na-e-maile-o-naruszeniu-praw-autorskich/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/10/prawa-autorskie-cyberalert-150x150.jpg">

## [⚠️ Uwaga na fałszywe doładowania telefonów w Plusie](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/uwaga-na-falszywe-doladowania-telefonow-w-plusie/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/10/cyberalert_plus-150x150.jpg">

## [Jak InPost zrobił wyciek danych Niebezpiecznikowi](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/jak-inpost-zrobil-wyciek-danych-niebezpiecznikowi/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/10/paczkomat-wyciek-150x150.jpg">

## [⚠️ Uwaga klienci ING, Paribas, Aliora i Santandera](https://web.archive.org/web/20250222063945/https://niebezpiecznik.pl/post/uwaga-klienci-ing-3/)
<img src="https://web.archive.org/web/20250222063945im_/https://niebezpiecznik.pl/wp-content/uploads/2024/10/cyberalert-ing-600x337.jpg">


"""
        )
