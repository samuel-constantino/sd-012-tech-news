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
    selector = Selector(text=html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()

    title = selector.css("h1.tec--article__header__title::text").get()

    timestamp = selector.css("time#js-article-date::attr(datetime)").get()

    writer = selector.css(".z--font-bold *::text").get()
    if writer:
        writer = writer.strip()

    shares_count = selector.css("div.tec--toolbar__item::text").get()
    if shares_count:
        shares_count = int(shares_count[:-15].strip())
    else:
        shares_count = 0

    comments_count = selector.css("button#js-comments-btn::text").getall()[1]
    comments_count = int(comments_count[:-13].strip())

    summary = "".join(selector.css(
        ".tec--article__body > p:nth-of-type(1) *::text"
    ).getall())

    sources_list = selector.css("div.z--mb-16 div a::text").getall()
    sources = []
    for source in sources_list:
        sources.append(source.strip())

    category_list = selector.css("div#js-categories a::text").getall()
    categories = []
    for category in category_list:
        categories.append(category.strip())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
