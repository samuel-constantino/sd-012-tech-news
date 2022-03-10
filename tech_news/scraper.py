import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        sleep(1)
    except requests.HTTPError:
        return None
    except requests.ReadTimeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    # news = []

    # for card_title in selector.css("h3.tec--card__title"):
    #     url = card_title.css("a.tec--card__title__link::attr(href)").get()
    #     news.append(url)

    cards_link = selector.css(
        "h3 a.tec--card__title__link::attr(href)"
    ).getall()
    return cards_link


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page_link = selector.css("a.tec--btn::attr(href)").get()

    if next_page_link is not None:
        return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
